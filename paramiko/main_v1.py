import time

import paramiko

from getpass import getpass

HOST = '192.168.0.113'
USER = 'root'
# USER = 'vik'


if __name__ == "__main__":
    try: 
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy( paramiko.AutoAddPolicy )

        password = getpass('Ingrese su contrasenna: ')
        client.connect(HOST, username=USER, password=password)

        stdin, stdout, stderr = client.exec_command('ls -al')
        time.sleep(1)

        result = stdout.read().decode()

        print(result)

        client.close()

    except paramiko.ssh_exception.AuthenticationException as e:
        print('Authentication failed')
