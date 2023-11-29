create database if not exists lesson14;

use lesson14;

create table if not exists users (
	id int primary key,  -- Уникальный идентификатор
	username varchar(64) not null,  -- длина 64 символа (обязательно для заполнения)
    password varchar(64) not null,
    email varchar(20) null unique
);

create table if not exists orders(
	id  int primary key,
    user_id int,
    product_id int,
    count int
);

create table if not exists products(
	id int primary key,
    name varchar(20),
    cost int,
    count int,
    seller_id int
);

create table if not exists seller(
	id int primary key,
    company varchar(60),
    phone int unique
);

alter table orders add foreign key (user_id) references users (id);
alter table orders add foreign key (product_id) references products (id);

alter table products add foreign key (seller_id) references seller (id);

select * from users;

select * from orders;

select * from products;

select * from seller
