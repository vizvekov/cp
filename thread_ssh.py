import threading
import paramiko

class TestThread(threading.Thread):
    
    stdout
    stderr
    connection = paramiko.SSHClient()
    config = {}
    
    def __init__(self,config):
	    self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.config = config
    
    def __connect(self):
        connection.connect(config['ext_ip'],username="root",password=config['password'])
    
    def run(self):
        self.__connect()
#    	print('my name',self.getName())
	
	
#test = TestThread()
#test.setName('my proc')
#test.setDaemon(True)
#test.start()
#time.sleep(20)