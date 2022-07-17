import threading
import time
import random
def thread(i):
    print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    randsleeptime = random.randint(1,10)
    time.sleep(randsleeptime)
    print("Thread {} stops sleeping {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

for i in range(10):
    t1 = threading.Thread(target=thread, args=(i,))
    t1.start()
    """
    print()
    print("Active Threads :", threading.activeCount())
    print()
    print("Thread Objects :", threading.enumerate())
    """