import paramiko
from getpass import getpass
import time

HOST = '192.168.1.1'
USER = 'root'

if __name__ == '__main__':
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy (paramiko.AutoAddPolicy())
        password = getpass('Password is printed at the back of the gateway: ')
        client.connect(HOST, username=USER, password=password)

        stdin, stdout, stderr = client.exec_command('cd /tmp/')
        stdin, stdout, stderr = client.exec_command('df -h')


        time.sleep(1)
        result = stdout.read().decode()
        print(result)
    except paramiko.ssh_exception.AuthenticationException as e:
        print('Autenticacion fallida')