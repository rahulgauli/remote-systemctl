import paramiko
import sys

class ConnectionException(Exception):
    pass


class Ssh_connect:
    
    def __init__(self,hostname, privatekey, username=None, timeout = None):
        self.hostname = hostname
        self.privatekey=privatekey
        self.username = username
        if timeout is None:
            self.timeout = 1500
        else:
            self.timeout = timeout
        self.sshclient = self.connect_remote()
   
        
        
    def connect_remote(self):
        
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname,key_filename=self.privatekey, username=self.username, timeout=self.timeout)
        return ssh

    
    
    
    @staticmethod
    def unit_parser(list_of_services):
        services = ""
        list_of_services = list_of_services.read().splitlines()
        for i in range(0,len(list_of_services)-7):
            aservice = list_of_services[i].decode("utf8")
            aservice = aservice.split(None)
            one = aservice[0]
            if len(services) == 0:
                services = services + one
            else:
                services = services + "\n" + one
#asdfasdfasdf
        return services
        


    def list_services(self):
        try:
            _, stdout, _ = self.sshclient.exec_command("systemctl list-units")
            services = self.unit_parser(stdout)
            return services
        except paramiko.SSHException as e:
            print("connection error")
            sys.exit()
    
    def start(self, service_name):
        _, stdout, stderr = self.sshclient.exec_command("sudo systemctl start {}".format(service_name))
        data = stderr.read().splitlines()
        print(data)
        if len(data)>0:
            return False
        if len(data)==0:
            return True
        
    def stop(self,service_name):
        _, stdout, stderr = self.sshclient.exec_command("sudo systemctl stop {}".format(service_name))
        data = stderr.read().splitlines()
        print(data)
        if len(data)>0:
            return False
        if len(data)==0:
            return True
        
    def restart(self,service_name):
        _, stdout, stderr = self.sshclient.exec_command("sudo systemctl restart {}".format(service_name))
        data = stderr.read().splitlines()
        if len(data)>0:
            return False
        if len(data)==0:
            return True
    def mask(self,service_name):
        _, stdout, stderr = self.sshclient.exec_command("sudo systemctl mask {}".format(service_name))
        data = stderr.read().splitlines()
        if len(data)>0:
            return False
        if len(data)==0:
            return True
    def unmask(self,service_name):
        _, stdout, stderr = self.sshclient.exec_command("sudo systemctl unmask {}".format(service_name))
        data = stderr.read().splitlines()
        if len(data)>0:
            return False
        if len(data)==0:
            return True
    def status(self,service_name):
        _, stdout, stderr = self.sshclient.exec_command("sudo systemctl status {}".format(service_name))
        data = stdout.read().splitlines()
        return data
        #a;kldgfhadsfkgjhas
        
        
