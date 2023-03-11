#!/bin/bash

echo "Hola mundo" >stdout.txt

echo "Hola, desde deploy en codigo cafilito con nginx y mysql" >>stdout.txt

# error

ls stdout.py

ls stdout.py 2>sterr.txt
ls stdout.py 2>>sterr.txt

ls stdout.txt >stdout.txt 2>stderr.txt
ls stdout.txt 1>stdout.txt 2>stderr.txt
