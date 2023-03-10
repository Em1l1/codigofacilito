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

        session = client.get_transport().open_session()
        if session.active:
            session.set_combine_stderr(True)
            # seudo terminal
            # session.get_pty()

            # ejecutar el comando
            session.exec_command('sudo ls -l')

            # obtener infomacion a traves de un canal
            # stdin = session.makefile('wb')
            stdout = session.makefile('rb')

            # password
            stdin.write( password + '\n')

            result = stdout.read().decode()

            print(result)


        client.close()

    except paramiko.ssh_exception.AuthenticationException as e:
        print('Authentication failed')
