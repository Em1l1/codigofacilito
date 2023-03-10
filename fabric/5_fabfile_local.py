from fabric.api import run, task, local

@task
def show_dir():
    local('ls -l')
