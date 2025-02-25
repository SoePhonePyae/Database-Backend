SELECT * FROM admin;

SELECT * FROM banned_members;

SELECT * FROM customer;

SELECT * FROM game;

SELECT * FROM game_reports;

SELECT * FROM notice;

SELECT * FROM payment;

SELECT * FROM rental;

SELECT * FROM staff;

------------

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

------
-- 1. Drop child tables first (those referencing others).
DROP TABLE IF EXISTS payment CASCADE;
DROP TABLE IF EXISTS game_reports CASCADE;
DROP TABLE IF EXISTS rental CASCADE;
DROP TABLE IF EXISTS banned_members CASCADE;
DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS staff CASCADE;
DROP TABLE IF EXISTS notice CASCADE;
DROP TABLE IF EXISTS game CASCADE;
DROP TABLE IF EXISTS admin CASCADE;

-- 2. Drop ENUM types after all tables are gone.
DROP TYPE IF EXISTS rental_status CASCADE;
DROP TYPE IF EXISTS staff_type CASCADE;
