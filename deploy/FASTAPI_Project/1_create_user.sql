--  instalar mysql
sudo apt install mysql-server

-- mysql cliente
sudo mysql

-- crear usuario
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Passwrod1234?!';

-- all privelges
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;

-- create database
create database fastapi_project;