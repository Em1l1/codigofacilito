from fabric.api import run, task, env, cd

env.hosts = ['ip', 'ip']
env.user = 'eduardo'
env.key_filename = '~/.ssh/id_rsa.pub'


@task
def pull():
    with cd('python-web')
        run('git pull')
