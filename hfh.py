import threading
import time 
def func(name):
    print(f'potok - {name}')
    time.sleep(4)
tread1=threading.Thread(target=func,args=('anna',))
tread2=threading.Thread(target=func,args=('eva',))
print('start -osnova')
tread1.start()
tread2.start()    
while tread1.is_alive() or tread2.is_alive():
    print(f"{tread1.name} жив: {tread1.is_alive()}, {tread2.name} жив: {tread2.is_alive()}")
    time.sleep(0.5) 
tread1.join()
tread2.join()
print('-')  

    


