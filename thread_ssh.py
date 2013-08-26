import time
import threading

class TestThread(threading.Thread):
    def run(self):
	print('my name',self.getName())
	
	
test = TestThread()
test.setName('my proc')
test.setDaemon(True)
test.start()
time.sleep(20)