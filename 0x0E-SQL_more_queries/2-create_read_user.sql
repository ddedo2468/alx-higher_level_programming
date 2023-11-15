-- creating the DB.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creating the user.
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grant all privilages to the user.
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;