import threading
counter = 0
lock = threading.Lock()

def inc(name):
    global counter
    lock.acquire()
    for i in range(1000):
        counter+=1
        print(name, counter)
    lock.release()

def dec(name):
    global counter
    lock.acquire()
    for i in range(1000):
        counter-=1
        print(name, counter)
    lock.release()
    
thread1 = threading.Thread(target=inc, args=('Thread-1-inc',))
thread2 = threading.Thread(target=inc, args=('Thread-2-inc',))
thread3 = threading.Thread(target=dec, args=('Thread-3-dec',))
thread4 = threading.Thread(target=dec, args=('Thread-4-dec',))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
print("Final Counter:", counter)

