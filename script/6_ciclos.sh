#!/bin/bash
# for
# for <variable> in <collection>
# do
#   <comandos>
# done

for numero in 1 2 3 4 5 6 7 8 9
do 
  if [[ $(( numero % 3 )) -eq 0 ]]; then
    echo $numero "es numero impar"
  fi
done

#while
# while [[  ]]
# do 
#   <comandos>
# done

contador=1
while [[ $contador -le 10 ]]; do
  echo $contador
  let "contador=contador+1"
done