'''Создайте два потока:

Первый поток должен выполнять задачу, которая занимает 3 секунды (например, имитация обработки данных).
Второй поток должен начать свою задачу только после того, как первый поток завершит свою работу.'''

import threading
import time
from concurrent.futures import ThreadPoolExecutor
event = threading.Event()
def func(name):
    print(f'Начал работу {name}')
    time.sleep(10)
    print(f'Закончил работу {name}')
    event.set()

def func1(name):
    
    print('wait')
    event.wait()
    print(f'run {name} ')
with ThreadPoolExecutor(max_workers=2) as executor:
    future1=executor.submit(func,'Ann') 
    future2=executor.submit(func1,'DAn') 
    future1.result()
    future2.result()


        

