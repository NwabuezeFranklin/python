import threading
import time
import random

def a(i):
    # Time was inversed at the first print just for the fun of it
    print("This func {} starts at {} ".format(i, time.strftime("%S:%M:%H", time.gmtime())))
    sleep = random.randint(1,5)
    time.sleep(sleep)
    print("Func {} stops executing at {}".format(i,time.strftime("%H:%M:%S", time.gmtime())))

for i in range(1,10):
    t2 = threading.Thread(target=a, args=(i, ))
    t2.start()
