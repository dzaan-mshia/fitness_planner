from sqlite3 import IntegrityError

from fastapi import HTTPException

from controllers.dto.UserDTO import UserDTO
from db.conf.db_configuration import create_connection


def get_user_by_username(username: str):
    connection = create_connection()
    try:
        cursor = connection.cursor()

        result = cursor.execute("""
        select id, password from users where username = ?
       """, (username,)).fetchone()

        if result is None:
            raise HTTPException(status_code=404, detail="Username not found!")
    finally:
        connection.close()

    return result


def save_user(data: UserDTO):
    user = (data.username, data.password)
    user_profile = (data.firstname, data.lastname, data.height, data.weight, data.age, data.gender)
    connection = create_connection()
    try:
        cursor = connection.cursor()

        cursor.execute("""
                insert into users(username, password) values (?, ?)
            """, user)

        new_user_id = cursor.lastrowid
        user_profile = (new_user_id, *user_profile)

        cursor.execute("""
            insert into user_profiles(user_id, firstname, lastname, height, weight, age, gender) 
            values (?, ?, ?, ?, ?, ?, ?)
        """, user_profile)

        connection.commit()
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Username in use!")
    finally:
        connection.close()
    return new_user_id
