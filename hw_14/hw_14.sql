create database if not exists lesson14;

use lesson14;
drop tables users, orders, products, seller;

create table if not exists users (
	id int primary key auto_increment,  -- Уникальный идентификатор
	username varchar(64) not null unique,  -- длина 64 символа (обязательно для заполнения)
    password varchar(64) not null,
    email varchar(20) not null unique
);

create table if not exists seller(
	id int primary key auto_increment,
    company varchar(60) not null,
    phone int not null unique
);

create table if not exists products(
	id int primary key auto_increment,
    name varchar(20) not null unique,
    cost int not null,
    count int not null,
    seller_id int,
    foreign key (seller_id) references seller (id)
);

create table if not exists orders(
	id  int primary key auto_increment,
    user_id int,
    product_id int,
    count int not null,
	foreign key (user_id) references users (id),
    foreign key (product_id) references products (id)
);

select * from users;

select * from orders;

select * from products;

select * from seller
