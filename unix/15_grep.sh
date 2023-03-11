!#/bash/sell
# busque de 3 caracteres
grep and frankenstein.txt

# buscar palabras
grep -w and frankenstein.txt

# maysculas y minusculas
grep -wi and frankenstein.txt

# numero de lineas
grep -win and frankenstein.txt

# musculas y minusculas
grep -wic and frankenstein.txt

# No se encuentra la palabra
grep -wivn and frankenstein.txt

grep -wivnm  10 and frankenstein.txt

grep -wivnm 10 and frankenstein.txt

grep -winm 10 and frankenstein.txt

# dos palabras
grep "he is as silent" frankenstein.txt

# lineas antres y despues
grep -n  "He sasw his" frankenstein.txt

grep -nB  "He sasw his" frankenstein.txt

grep -nA  "He sasw his" frankenstein.txt

grep -nC  "He saw his" frankenstein.txt

# part 3
grep -win sea frankenstein.txt

grep -wine sea -wine passage frankenstein.txt

grep -wine sea -wine passage -wine "He saw his" frankenstein.txt

