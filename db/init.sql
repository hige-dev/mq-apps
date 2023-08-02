CREATE ROLE app WITH PASSWORD 'password';
CREATE DATABASE app;
GRANT ALL PRIVILEGES ON DATABASE app TO app;
\c app

CREATE TABLE users (
    id serial primary key,
    name varchar(255),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
