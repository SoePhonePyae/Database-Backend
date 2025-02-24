CREATE DATABASE game_rent;

\c game_rent;  -- Connect to game_rent database

CREATE TABLE Admin (
admin_id SERIAL PRIMARY KEY,
admin_name VARCHAR(255) NOT NULL,
email VARCHAR(255) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL
);

CREATE TYPE staff_type AS ENUM ('Part_Time', 'Full_Time', 'Internship');

CREATE TABLE Staff (
staff_id SERIAL PRIMARY KEY,
staff_name VARCHAR(255) NOT NULL,
email VARCHAR(255) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL,
phone_number VARCHAR(20) NOT NULL,
salary NUMERIC(10,2) NOT NULL,
street_address VARCHAR(255) NOT NULL,
city VARCHAR(100) NOT NULL,
state VARCHAR(100) NOT NULL,
zip_code VARCHAR(20) NOT NULL,
type staff_type NOT NULL,
admin_id INT NOT NULL,
last_action VARCHAR(100),
CONSTRAINT fk_admin FOREIGN KEY (admin_id) REFERENCES Admin(admin_id)
ON UPDATE CASCADE
ON DELETE RESTRICT
);


CREATE TABLE Customer (
customer_id SERIAL PRIMARY KEY,
customer_name VARCHAR(255) NOT NULL,
email VARCHAR(255) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL,
phone_number VARCHAR(20) NOT NULL,
street_address VARCHAR(255) NOT NULL,
city VARCHAR(100) NOT NULL,
state VARCHAR(100) NOT NULL,
zip_code VARCHAR(20) NOT NULL,
staff_id INT NOT NULL,
created_date DATE,
CONSTRAINT fk_staff FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
ON UPDATE CASCADE
ON DELETE RESTRICT
);


CREATE TABLE Banned_Members (
ban_id SERIAL,
customer_id INT,
reason TEXT NOT NULL,
ban_date DATE NOT NULL,
PRIMARY KEY (ban_id, customer_id),
CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
ON UPDATE CASCADE
ON DELETE CASCADE
);


CREATE TABLE Notice (
notice_id SERIAL PRIMARY KEY,
reason TEXT NOT NULL,
date DATE NOT NULL,
admin_id INT NOT NULL,
CONSTRAINT fk_admin_notice FOREIGN KEY (admin_id) REFERENCES Admin(admin_id)
ON UPDATE CASCADE
ON DELETE RESTRICT
);


CREATE TABLE Game (
game_id SERIAL PRIMARY KEY,
game_name VARCHAR(255) NOT NULL,
release_date DATE NOT NULL,
platform VARCHAR(100) NOT NULL,
genre VARCHAR(100) NOT NULL,
rating VARCHAR(20) NOT NULL,
stock_number INT NOT NULL,
price INT NOT NULL,
image_link VARCHAR(255) NOT NULL,
admin_id INT NOT NULL,
last_action VARCHAR (100),
CONSTRAINT fk_admin_game FOREIGN KEY (admin_id) REFERENCES Admin(admin_id)
ON UPDATE CASCADE
ON DELETE RESTRICT
);

CREATE TYPE rental_status AS ENUM ('Pending', 'Renting', 'Returned');

CREATE TABLE Rental (
rental_id SERIAL PRIMARY KEY,
game_id INT NOT NULL,
customer_id INT NOT NULL,
status rental_status NOT NULL,
rent_date DATE NOT NULL,
due_date DATE NOT NULL,
duration INT,
CONSTRAINT fk_game FOREIGN KEY (game_id) REFERENCES Game(game_id)
ON UPDATE CASCADE
ON DELETE RESTRICT,
CONSTRAINT fk_customer_rental FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
ON UPDATE CASCADE
ON DELETE RESTRICT
);


CREATE TABLE Payment (
payment_id SERIAL,
rental_id INT,
proof VARCHAR(255) NOT NULL,
method VARCHAR(50) NOT NULL,
PRIMARY KEY (payment_id, rental_id),
CONSTRAINT fk_rental FOREIGN KEY (rental_id) REFERENCES Rental(rental_id)
ON UPDATE CASCADE
ON DELETE CASCADE
);


CREATE TABLE Game_Reports (
report_id SERIAL PRIMARY KEY,
rental_id INT NOT NULL,
reason TEXT NOT NULL,
report_date DATE NOT NULL,
detail TEXT NOT NULL,
attachment VARCHAR(255),
CONSTRAINT fk_rental_report FOREIGN KEY (rental_id) REFERENCES Rental(rental_id)
ON UPDATE CASCADE
ON DELETE RESTRICT
);
