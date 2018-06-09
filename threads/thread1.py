import threading
import time

def hello():
    print ("Hello Thread")
    print(threading.currentThread().getName())
    time.sleep(3)
    for i in range(1,5):
        print ("i is ", i,"\n")
        time.sleep(1)

def hi():
    print ("Hi Thread")
    time.sleep(2)
    print(threading.currentThread().getName())
    for j in range(1,5):
        print ("j is ", j,"\n")
        time.sleep(1)
    
hello1 = threading.Thread(target=hello,name="Hello1")
hi1 = threading.Thread(target=hi,name="Hi1")
hi2 = threading.Thread(target=hi,name="Hi2")
hi1.start()
hello1.start()
hi2.start()