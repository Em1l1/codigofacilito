# Instalar mysql
sudo apt install mysql-server

# Instalar el cliente libmysqlclient-dev
sudo apt-get install libmysqlclient-dev

# create new user mysql
CREATE USER 'eduardo'@'localhost' IDENTIFIED BY ''

# aLL PRIVILEGES
GRANT ALL PRIVILEGES ON *.* TO 'EDUARDO'@'localhost'
# autenticacion
mysql -u ed

# ver tablas
show databases

# CREATE database
CREATE DATABASE project_web_facilito
