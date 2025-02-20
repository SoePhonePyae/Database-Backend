CREATE DATABASE game_rent;

USE game_rent;

CREATE TABLE Admin (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
 
 
CREATE TYPE staff_type AS ENUM ('Part_Time', 'Full_Time', 'Internship')
 
CREATE TABLE Staff (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
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
    last_action_on TIMESTAMP,
    CONSTRAINT fk_admin FOREIGN KEY (admin_id) REFERENCES Admin(id)
	ON UPDATE CASCADE
	ON DELETE RESTRICT
);
 
 
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    staff_id INT NOT NULL,
    joined_date DATE
	CONSTRAINT fk_staff FOREIGN KEY (staff_id) REFERENCES Staff(id)
	ON UPDATE CASCADE
	ON DELETE RESTRICT
);
 
 
CREATE TABLE Banned_Members (
    id SERIAL,
    customer_id INT,
    reason TEXT NOT NULL,
    ban_date DATE NOT NULL,
	PRIMARY KEY (id, customer_id),
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES Customer(id) 
	ON UPDATE CASCADE
	ON DELETE CASCADE
);
 
 
CREATE TABLE Notice (
    id SERIAL PRIMARY KEY,
    reason TEXT NOT NULL,
    date DATE NOT NULL,
    admin_id INT NOT NULL,
    CONSTRAINT fk_admin_notice FOREIGN KEY (admin_id) REFERENCES Admin(id) 
	ON UPDATE CASCADE
	ON DELETE RESTRICT
);
 
-- 
CREATE TABLE Game (
    game_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    release_date DATE  NOT NULL,
    platform VARCHAR(100)  NOT NULL,
    genre VARCHAR(100)  NOT NULL,
    content_rating VARCHAR(20)  NOT NULL,
    stock INT NOT NULL,
    image_link VARCHAR(255)  NOT NULL,
    admin_id INT NOT NULL,
    last_action VarChar(50) NOT NULL,
    CONSTRAINT fk_admin_game FOREIGN KEY (admin_id) REFERENCES Admin(id) 
	ON UPDATE CASCADE
	ON DELETE RESTRICT
);

 
CREATE TYPE rental_status AS ENUM ('Pending', 'Renting', 'Returned');

 
CREATE TABLE Rental (
    id SERIAL PRIMARY KEY,
    game_id INT NOT NULL,
    customer_id INT NOT NULL,
    status rental_status NOT NULL,
    rent_date DATE NOT NULL,
    due_date DATE NOT NULL,
    duration INT,
    CONSTRAINT fk_game FOREIGN KEY (game_id) REFERENCES Game(id)
	ON UPDATE CASCADE
	ON DELETE RESTRICT,
    CONSTRAINT fk_customer_rental FOREIGN KEY (customer_id) REFERENCES Customer(id)
	ON UPDATE CASCADE
	ON DELETE RESTRICT
);
 
 
CREATE TABLE Payment (
    id SERIAL,
    rental_id INT,
    proof VARCHAR(255) NOT NULL,
    method VARCHAR(50) NOT NULL,
	PRIMARY KEY (Payment_ID, Rental_ID),
    CONSTRAINT fk_rental FOREIGN KEY (rental_id) REFERENCES Rental(id) 
	ON UPDATE CASCADE
	ON DELETE CASCADE
);
 

--Correct
CREATE TABLE Game_Reports (
    report_id SERIAL PRIMARY KEY,
    rental_id INT NOT NULL,
    reason TEXT  NOT NULL,
    report_date DATE  NOT NULL,
    detail TEXT  NOT NULL,
    attachment VARCHAR(255),
    CONSTRAINT fk_rental_report FOREIGN KEY (rental_id) REFERENCES Rental(id)
	ON UPDATE CASCADE
	ON DELETE RESTRICT
);
 

