#!/bin/bash

# First 
# echo "Ingresa tu nombre: "
# read nombre

# echo "Ingresa tu edad: "
# read edad

# second
read -p "Ingresa tu nombre: " nombre
read -p "Ingresa tu edad: " edad

read -sp "Ingresa tu contrasena: " password

echo "\n"

echo "Hola" $nombre " tienes la edad de " $edad " annos." 
echo "password" $password