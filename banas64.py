import threading
import random
import time

class custThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        getTime(self.name)

        print("Thread", self.name, "Execution ends")

def getTime(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S",time.gmtime())))
    randSleeptime = random.randint(1,5)
    time.sleep(randSleeptime)

t1 = custThread('1')
t2 = custThread('2')
t1.start()
t2.start()

print("Thread 1 alive: ", t1.is_alive())
print("Thread 2 alive:", t2.is_alive())

