from fabric.api import run,  sudo, task, put, get

def pull():
    print('Obtenermos todos los cambios de la rama master')


@task(alias='dp')
def deploy():
    pull()

# Enviar archivo
@task
def upload_txt_file():
    put(
        local_path='./example.txt',
        remote_path='./python-web'
    )


# Descargar archivo
@task
def get_txt_file(file):
    get(
        local_path='./descargas',
        remote_path=f'./python-web/{file}',
    )
