import threading
mythreadpool = threading.BoundedSemaphore(value=4)

def myfunction1():
    mythreadpool.acquire()
    print("function1")

def myfunction2():
    mythreadpool.acquire()
    print("function2")


t1 = threading.Thread(target = myfunction1)
t1.start()
t2 = threading.Thread(target = myfunction2)
t2.start()
t3 = threading.Thread(target = myfunction1)
t3.start()
t4 = threading.Thread(target = myfunction2)
t4.start()
t5 = threading.Thread(target = myfunction1)
t5.start()