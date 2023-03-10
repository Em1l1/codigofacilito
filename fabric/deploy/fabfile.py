from datetime import datetime
from fabric.api import run, task, env, cd, prefix, sudo, get, local

# entornos
env.hosts = ['ip']
env.user = 'eduardo'

# variasbles 
DATABASE = 'project_web_facilito'
BACKUP_FOLDER = './descargas'

# git pull
def pull():
    run('git pull')


# Instalar dependecias al prjecto
def install_requirements():
    run('pip install -r requiremnts.txt')

# deploy project
@task
def deploy():
    with cd('python-web'):
        pull()

        with prefix('source env/bin/activate'):
            innstall_requirements()


        sudo('systemctl restart python-web')
        sudo('systemctl restart nginx')


# Descargar el respoldo
def get_backup(backup) :
    get(
        remote_path=backup,
        local_path=BACKUP_FOLDER
    )


# fecha en que se creo el respaldo
def get_backup_name():
    # database_dia_mes_ano.sql
    return f'{DATABASE}_{ datatime.now().strftime("%d_%m_%Y") }.sql'


# configurar backup en local
def load_backup(backup_path):
    local(f'mysql -u root -e "DROP DATABASE {DATABASE}"')
    local(f'mysql -u root -e "CREATE DATABASE {DATABASE}"')

    local(f'mysql -u root {DATABASE} < {backup_path}')


# remover backup
def delete_backup(backup):
    sudo(f'rm {backup}')



# copiar el respando al projecto local
def create_back(backup_name):
    run(f'mysqldump -u eduardo {DATABASE} > {backup_name}')


# respaldo de base de datos
@task
def backup():
    backup_name = get_backup_name()
    # run('mysqldump -u eduardo --password=passwrod database > backup.sql')
    # sin contrasenna
    # run(f'mysqldump -u eduardo {DATABASE} > backup.sql')

    create_back(backup_name)

    get_backup(backup_name)
    backup_path = f'{BACKUP_FOLDER}{backup_name}'
    load_backup(backup_path)
    delete_backup(backup_name)
