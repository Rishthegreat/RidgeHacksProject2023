create table users (
    uuid integer primary key,
    username text not null,
    password_hash text not null,
    email text not null,
    first_name text not null,
    last_name text not null
);
