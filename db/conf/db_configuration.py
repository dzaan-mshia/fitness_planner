import sqlite3
from sqlite3 import Connection


def create_connection() -> Connection:
    connect = sqlite3.connect("fitness.db")
    return connect


def init_db():
    connection = create_connection()
    cursor = connection.cursor()
    create_user_table(cursor)
    create_user_profile_table(cursor)
    connection.commit()
    connection.close()


def create_user_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT unique NOT NULL,
    password TEXT NOT NULL
    )
    """)


def create_user_profile_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profiles (
        user_id integer ,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        weight float NOT NULL,
        height integer NOT NULL,
        age integer not null ,
        gender text not null ,
        FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)
