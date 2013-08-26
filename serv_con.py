import paramiko
from thread_ssh import sshThread




class sshConnect:

    configs = {}


    def __init__(self):
	    pass

    def add_conn(self,server):
        self.configs.update({server['ext_ip']: sshThread(server)})

    def get_server_count(self):
        return len(self.configs)

    def send_comand(self,command):
	    for ip, thread in self.configs.items():
            thread.command = command
            thread.setName('ssh to ' + ip)
            thread.setDaemon(True)
            thread.start()

    def  __del__(self);
	    for ip, thread in self.connections.items():
	        del thread
