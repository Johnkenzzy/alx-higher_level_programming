-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa).

-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created or existing database
USE hbtn_0d_usa;

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
