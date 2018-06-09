import threading
import logging

def threadwith(lock):
    with lock:
        print('\n Lock With Block \n')
        for i in range(5):
            print (i)
        print(threading.currentThread().getName())
        
def threadacquire(lock):
    lock.acquire()
    try:
        print('\n Lock Acquire Block \n')
        for i in range(5):
            print (i)
        print(threading.currentThread().getName())
    finally:
        lock.release()


lock = threading.Lock()
tw = threading.Thread(target=threadwith, args=(lock,))
ta = threading.Thread(target=threadacquire, args=(lock,))

tw.start()
ta.start()