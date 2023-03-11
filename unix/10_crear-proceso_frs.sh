#!/bin/bash
python main.py

# Proceos en segundo plano
nvim &

# verificar los programas en segundo plano
jobs

# colocarlo en primer plano
fg % 1
