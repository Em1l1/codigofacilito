# Ejecutar en un servidor remoto
# sudo, super usuario 
from fabric.api import run, sudo 

def show_dir():
    run('ls')


# establecer parametros
def create_folder(folder):
    run(f'mkdir {folder}')

def delete_folder(folder):
    sudo(f'rm -rf {folder}')
