from paramiko import SSHClient
import paramiko
import model

class HostFinder(object):
    def __init__(self,host='ian.ucsd.edu',port=9000):
        self.r = model.RedisModel()

    def find_hostname(self, ip):
        result = self.r.getHostname(ip)
        if not result: 
            ssh = paramiko.SSHClient()
            ssh.connect(ip, username="idfoster")
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("hostname")
            result = ssh_stdin
            self.r.addHostname(ip, result)
        else:
            return result
