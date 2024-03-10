CREATE SEQUENCE user_id_seq;

create TABLE users
(
    id       int DEFAULT nextval('user_id_seq'::regclass) primary key,
    username varchar(64) unique,
    password varchar(64)
);

create table user_profiles
(
    user_id   int references users (id),
    firstname varchar(32),
    lastname  varchar(32),
    age       smallint,
    weight    smallint,
    height_cm smallint,
    sex       varchar
)
