import threading
import paramiko

class sshThread(threading.Thread):
    
    stdout
    stderr
    stdin
    connection = paramiko.SSHClient()
    config = {}
    command 
    
    def __init__(self,config):
	    self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.config = config
    
    def __run_command(self):
        self.stdin, self.stdout, self.stderr = self.connection.exec_command(command)
    
    def __connect(self):
        self.connection.connect(config['ext_ip'],username="root",password=config['password'])
    
    def run(self):
        self.__connect()
        self.__run_command()
        connection.close()
#    	print('my name',self.getName())
	
	
#test = TestThread()
#test.setName('my proc')
#test.setDaemon(True)
#test.start()
#time.sleep(20)