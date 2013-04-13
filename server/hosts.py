from paramiko import SSHClient
import paramiko
import model

class HostFinder(object):
    def __init__(self,host='ian.ucsd.edu',port=9000):
        self.r = model.RedisModel()

    def find_hostname(self, ip):
        result = self.r.getHostname(ip)
        if not result: 
            #try:
                ssh = paramiko.SSHClient()
                ssh.load_system_host_keys()
                ssh.connect(ip, username="idfoster")
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("hostname")
                result = ssh_stdin
                self.r.addHostname(ip, result)
            #except:
            #    pass
        else:
            return result
