create table users (
    users_uuid integer primary key,
    username text not null,
    password_hash text not null,
    email text not null,
    first_name text not null,
    last_name text not null,
    location text not null
);

create table requests (
    requests_uuid integer primary key autoincrement,
    user_uuid integer not null,
    request_type text not null,
    cost decimal not null,
    brand text not null,
    part text not null,
    is_solved boolean not null,
    request_time timestamp not null,
    foreign key (user_uuid) references users (users_uuid)
);

create table matches (
    matches_uuid integer primary key autoincrement,
    receiver_request_uuid integer not null,
    sender_request_uuid integer not null,
    foreign key (receiver_request_uuid) references requests (requests_uuid),
    foreign key (sender_request_uuid) references requests (requests_uuid)
);