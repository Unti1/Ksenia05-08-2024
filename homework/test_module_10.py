import math
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
q=Queue()
x=[[1,2],[3,4],[5,6],[7,8]]
def func(x):
    for n in x:
        if n <= 1:
            return f'{n-True}'
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return f'{n-True}'
    return f'{n-False}'

with ThreadPoolExecutor(max_workers=4) as executor:
    result=executor.map(func,x)
    for x in result:
        print(x)
        q.put(x)
''' Пул потоков для скачивания файлов
- Создайте пул из 5 потоков (на основе собственного класса, наследующего Thread).
- Задачи (URL файлов) добавляются в Queue.
- Каждый поток скачивает файл и сохраняет его на диск.
- Реализуйте ограничение на максимальное количество одновременно скачиваемых файлов.
.
'''


import threading
import time
from queue import Queue
q=Queue(maxsize=3)
disk=[]

class th(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        while not q.empty():
            x=q.get(timeout=2) 
            print(f'{self.name} скачивает файл {x}...')
            time.sleep(2)
            print(f'Файл {x} записан на диск')
            q.task_done()
def x():
    for x in range(10):
        xx=f'file{x}.py'
        q.put(xx) 

thh=[]   
th2=threading.Thread(target=x)
th2.start()

for x in range(5):
    th1=th(f'Поток {x}')
    th1.start()
    thh.append(th1)

for x in thh:
    x.join()
th2.join()   
    


'''Банковские транзакции с синхронизацией
- Создайте 10 потоков, имитирующих клиентов банка.
- Каждый поток выполняет 100 операций (пополнение/снятие) с общим счетом.
- Используйте Lock для защиты общего баланса от состояния гонки.
'''

import threading
from concurrent.futures import ThreadPoolExecutor
import time
from queue import Queue
import random

lock=threading.Lock()

balance=0
def plus():
    global balance
    x=random.randint(1,100)
    with lock:
        balance+=x
        time.sleep(2)
        print(f'{balance} увеличен на {x}')
def min():
    global balance
    x=random.randint(1,100)
    with lock:
        if x>balance:
            print('Недостаточно средств')
        else:
            balance-=x
            time.sleep(2)
        print(f'{balance} уменьшен на {x}')

with ThreadPoolExecutor(max_workers=10) as executor:
    future1=[executor.submit(plus) for _ in range(1,10)]
    future2=[executor.submit(min) for _ in range(1,10)]
    for f in future1:
        f.result()
    for f in future2:
        f.result()


        
'''Producer-Consumer через Pipe
- Создайте два процесса: Producer генерирует случайные числа (1–100).
- Consumer вычисляет их квадраты.
- Обмен данными организуйте через Pipe.
- Добавьте задержку в 1 секунду для Consumer.
'''
from multiprocessing import Process,Pipe,Pool
import random
import time
def producer(pipe):
    x=random.randint(1,101)
    pipe.send(x)
    print(f'{x}-отправлен')

def consumer(pipe):
    x=pipe.recv()
    print(f'Получили {x}\nОбработка ')
    x=x**2
    time.sleep(2)
    print(f'Получилось {x}')

if __name__=='__main__':
    pipe1,pipe2=Pipe()
    p=Process(target=producer,args=(pipe1,))
    p1=Process(target=consumer,args=(pipe2,))
    p.start()
    p1.start()
    p.join()
    p1.join()

'''Поиск слова в файлах
- Запустите 3 потока для поиска слова "Python" в разных текстовых файлах.
- Каждый поток возвращает список строк с совпадениями через Queue.
- Реализуйте таймаут (например, 10 сек) на поиск в одном файле.

'''

import threading
import time
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
q=Queue()
lock=threading.Lock()
x=['tests1.txt','hfhdddddfff.txt','hfhddfff.txt','updated.txt']

def func(x):
    with open(x,'r') as file:
        print(f'Началась обработка файла {file}')
        time.sleep(2)
        x=file.read().split('\n')
        
        for xx in x:
            if 'Python' in xx:
                with lock:
                    q.put(xx)
                
        print('Готово')    

        

with ThreadPoolExecutor(max_workers=3) as executor:
    result=executor.map(func,x)
while not q.empty():
    print(q.get())

'''9. Распределенный расчет статистики
- Разделите список чисел на 4 части.
- Запустите 4 процесса, каждый вычисляет среднее значение своей части.
- Главный процесс объединяет результаты и вычисляет общее среднее.
- Используйте multiprocessing.Queue для передачи данных.

'''

from multiprocessing import Queue,Process,Lock
lock=Lock()
x=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

q=Queue()
def func(x,q):
    with lock:
        x1=sum(x)/len(x)
        
        q.put(x1)

if __name__=='__main__':
    pp=[]
    x1=0
    for _ in range(4):
        p=Process(target=func,args=(x[x1],q))
        p.start()
        pp.append(p)
        x1+=1
    for x in pp:
        x.join()    

        
while not q.empty():
    print(q.get())        

''' Диалог процессов через Pipe
- Создайте два процесса: ProcessA и ProcessB.
- ProcessA отправляет сообщение "Hello", ProcessB отвечает "World".
- Повторите обмен 5 раз, выводя результат каждого шага.
'''

from multiprocessing import Pipe,Process,Pool

def func(pipe):
    pipe.send('Hello')
    print('Отправил')
    print(pipe.recv())
def func1(pipe):
    x=pipe.recv()
    print('Получил и исправил')
    x+=' World!'
    pipe.send(x)
if __name__=='__main__':
    pipe1,pipe2=Pipe()
    p1=Process(target=func,args=(pipe1,))
    p2=Process(target=func1,args=(pipe2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

''' Приоритетная очередь задач
- Реализуйте многопоточную систему с очередью задач, где каждая задача имеет приоритет (1–5).
- Потоки-воркеры обрабатывают задачи в порядке приоритета.
- Используйте PriorityQueue из модуля queue.

'''

import queue
import threading
q=queue.PriorityQueue()

def func():
    while not q.empty():
        print('Обработка очереди')
        print(q.get())
        q.task_done()

q.put((1,'10'))
q.put((2,'20'))
q.put((5,'30'))
q.put((3,'40'))
q.put((4,'50'))
th=[]    
for _ in range(3):
    t=threading.Thread(target=func)  
    t.start()
    th.append(t)
for t in th:
    t.join()    

'''13. Игра «Скачки»
- Запустите 5 потоков-«лошадей», каждый двигается на случайное расстояние за шаг.
- Используйте Event для одновременного старта.
- Выводите позиции лошадей в реальном времени с синхронизацией вывода.
'''
from threading import Event,Thread
import time
import random
event=Event()
def func(name):
    print(f'Лошадь {name} готова')
    event.wait()
    for _ in  range(10):
        x=random.randint(0,10)
        print(f'Лощадь {name} сделала {x} за шаг')

th=Thread(target=func,args=('Eva',))  
th1=Thread(target=func,args=('Anna',)) 
th2=Thread(target=func,args=('Iva',)) 
th.start()
th1.start()
th2.start()
time.sleep(5)
print('Вперед!')
event.set()
th.join()
th1.join()
th2.join()


''' Распределенная сортировка
- Разделите большой список чисел на 4 части.
- Отсортируйте каждую часть в отдельном процессе.
- Объедините результаты в главном процессе, используя алгоритм слияния (merge).
- Для передачи данных используйте multiprocessing.Pipe.
'''

import multiprocessing
import numpy as np
x=[]
for i in range(100):
    x.append(i)

xx=np.array_split(x,4)

def func(x,pipe):
    pipe.send(x)

  
if __name__=='__main__':
    pipe,pipe1=multiprocessing.Pipe()
    pipe2,pipe3=multiprocessing.Pipe()
   
    st1=multiprocessing.Process(target=func,args=(xx[0],pipe))
    st2=multiprocessing.Process(target=func,args=(xx[1],pipe))
    st3=multiprocessing.Process(target=func,args=(xx[2],pipe2))
    
    st4=multiprocessing.Process(target=func,args=(xx[3],pipe2))
    
    
    st1.start()
    st2.start()
    st3.start()
    st4.start()

    st1.join()
    st2.join()
   
    x=pipe1.recv()
    x1=pipe1.recv()
    x2=pipe3.recv()
    x3=pipe3.recv()
    print(x,x1,x2,x3)

 '''Многопроцессорная обработка изображений
- Запустите 4 процесса через multiprocessing.Process.
- Каждый процесс применяет фильтр (например, инверсия цвета) к разным изображениям.
- Используйте multiprocessing.Queue для передачи путей к изображениям.

'''
from multiprocessing import Process,Queue, Pool,Lock
from PIL import Image
import numpy as np
lock=Lock()
def invert_colors(q):
    while not q.empty():
            x=q.get()
            image = Image.open(x)
            image_array = np.array(image)
            inverted_image_array = 255 - image_array
            inverted_image = Image.fromarray(inverted_image_array)
            inverted_image.save(x)
            inverted_image.show()
        

x=['/Users/ksenia/Downloads/photo_2025-01-31 11.59.55.jpeg','/Users/ksenia/Downloads/photo_2025-01-31 11.59.59.jpeg','/Users/ksenia/Downloads/photo_2025-01-31 12.00.00.jpeg']

if __name__=='__main__':
    q=Queue()
    
    for xx in x:
        q.put(xx)
    x=0
    thread=[]
    for _ in range(2):
        p=Process(target=invert_colors,args=(q,))
        thread.append(p)
        p.start()
    for tth in thread:
        tth.join()  
   
