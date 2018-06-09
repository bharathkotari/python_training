import threading, queue

def func1(num, q):
    while num < 1000:
        num =  num**2
        print(threading.currentThread().getName())
        q.put(num)
        print ("sending function",num,'\n')
    
def func2(num, q):
    while num < 1000:
        print(threading.currentThread().getName())
        num = q.get()
        print ("in function2",num,'\n')
num = 2
q = queue.Queue()
thread1 = threading.Thread(target=func1,args=(num,q),name='T1')
thread2 = threading.Thread(target=func2,args=(num,q),name='T2')
thread1.start()
thread2.start()
#thread1.join()
#thread2.join()