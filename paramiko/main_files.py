import scp
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

        # scp
        scp_client = scp.SCPClient( client.get_transport() )

        # Enviar archivos
        # scp_client.put(
        #     'README.md',
        #     '/home/vik/paraminko/'
        # )

        # Descargar archivos
        scp_client.get(
            '/home/vik/paraminko/server.conf',
            'descargas/'
        )

        # SFTP
        # Enviar archivo al servidor
        sftp_client = client.open_sftp()

        sftp_client.put(
            'README.md',
            '/home/vik/example/README.md'
        )

        # Descargar archivos de servidor
        sftp_client.get(
            '/home/vik/example1/servidor.md',
            'descargas/servidor.md'
        )

        # canales, se ejecutan una vez
        session = client.get_transport().open_session()
        if session.active:
            # session.exec_command('cd example && ls -l')
            session.exec_command('cd paraminko && ls -l')

            result = session.recv(1024).decode()
            print(result)

        scp_client.close()    
        sftp_client.close()
        client.close()

    except paramiko.ssh_exception.AuthenticationException as e:
        print('Authentication failed')
