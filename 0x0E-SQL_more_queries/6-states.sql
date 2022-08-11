-- States table
-- Script that creates the database hbtn_od_usa and the table states.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE,
	name VARCHAR(256) NOT NULL);