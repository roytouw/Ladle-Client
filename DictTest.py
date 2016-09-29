import threading

import time


def test():
    for i in range(1000):
        print(i)

def test2():
    for i in reversed(range(1000)):
        print(i)

t1 = threading.Thread(target=test)
t2 = threading.Thread(target=test2)
t1.start()
t2.start()
t1.join()
t2.join()
