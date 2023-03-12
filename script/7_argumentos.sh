#!/bin/bash
echo "Listado de argumentos: "

# echo $@
# echo $0
# echo $1
# echo $2
# echo $3
for argumento in $@; do
  echo $argumento
done