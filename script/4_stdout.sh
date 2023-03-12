#!/bin/bash

# wc 3_stdout.sh
stdout=$(wc 1_script.sh) # Vamos a almacenar el STDOUT  de un proceso
echo "La salida del comando wc es: " $stdout