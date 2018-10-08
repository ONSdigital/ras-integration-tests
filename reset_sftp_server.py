import paramiko

from config import Config

if __name__ == '__main__':
    print('Resetting sftp server')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=Config.SFTP_HOST,
                port=int(Config.SFTP_PORT),
                username=Config.SFTP_USERNAME,
                password=Config.SFTP_PASSWORD,
                look_for_keys=False,
                timeout=120)
    sftp = ssh.open_sftp()

    files = sftp.listdir(path=Config.SFTP_DIR)
    for file in files:
        path = f"{Config.SFTP_DIR}/{file}"
        try:
            sftp.remove(path)
        except FileNotFoundError:
            print("Can't find file " + path)

    sftp.close()
    ssh.close()

    print('Successfully reset sftp server')
