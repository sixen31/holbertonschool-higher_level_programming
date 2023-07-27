-- Create user 'user_0d_1' with all privileges
-- Password for user set as 'user_0d_1_pwd'
-- If user already exists, script should not fail
-- script that the mysql server user 1
-- Script that creates an user in MySQL server
-- Query to create the user 'user_0d_1' in MySQL server

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
