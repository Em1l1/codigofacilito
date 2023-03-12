#!/bin/bash

# if <Condiciones>
# then
#   <Comandos>
# else
#   <Comandos>
# fi

# ()
# (( ))
# []
# [[ ]]
read -p "Ingresa tu username: " username
read -p "Ingresa tu edad: " edad

# if [[ $username == "Cody" ]]

# -gt -> >
# -lt -> <
# -ge -> >=
# -le -> <=
# -eq -> ==
# -ne -> !=

# if [[ $username -ne "Cody" && $username ]]
if [[ $username != "Cody" ]] && [[ $edad -ge 18 ]]; then
  echo "Hola, usuario" $username
  echo "Ya puedes tramitar tu licencia de manejo"
else
  echo "Hola, Cody, que gusto de saludarte"
  echo "Aun no puedes tramitar tu licencia de manejo"
fi

