
from fabric.api import run, task, cd, prefix

# cd
@task
def pull():
    run('cd python web && git pull')
    # Ejecutar varios comandos
    # run se ejecuta independient
    # with cd ('python-web')
        # run('git pull')


@task
def install_requirements():
    # run('cd python-web && source env/bin/activate && pip install -r requirements.txt')
    with cd('python-web'):
        with prefix('source env/bin/activate'):
            run('pip install -r requirements.txt')
