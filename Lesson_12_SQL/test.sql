create database lesson14;
use lesson14;
create table users(
	id int unsigned primary key auto_increment,
    username varchar(64) unique not null,
    password varchar(64) not null,
    email varchar(30) null
);


create table orders(
	id int unsigned primary key auto_increment,
    user_id int unsigned not null,
    product_id int unsigned not null,
    count int unsigned,

    foreign key (user_id) references users (id),
    foreign key (product_id) references users (id)
);

create table products(
	id int unsigned primary key auto_increment,
    name varchar(25) unique not null,
    cost int not null,
    count int,
    seller_id int unsigned,

    foreign  key (seller_id) references seller (id)
);


create table seller(
	id int unsigned primary key auto_increment,
    company varchar(64) unique not null,
    phone varchar(20) null
);