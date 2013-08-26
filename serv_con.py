import paramiko





class sshConnect:

    connections = {}


    def __init__(self):
	    pass

    def add_conn(self,server):
	    self.connections.update(server['ext_ip']: paramiko.SSHClient()})
	    self.connections[server['ext_ip']].set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    self.connections[server['ext_ip']].connect(server['ext_ip'],username="root",password=server['password'])

    def send_comand(self,comand):
	for ip, connect in self.connections.items():
	    stdin, stdout, stderr = connect.exec_command(comand)
	    self.stdout.update({ip: stdout})
	    self.stderr.update({ip: stderr})

    def  __del__(self);
	for ip, connect in self.connections.items():
	    connect.close()
