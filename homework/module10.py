'''Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - 
название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.

Пример результата выполнения программы:
Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков
Вывод на консоль:
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа потоков 0:00:34.003411 # Может быть другое время
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков 0:00:20.071575 # Может быть другое время

Записанные данные в файл должны выглядеть так:'''
import time 
import threading

def write_words(word_count, file_name):
    with open(file_name,'w') as file:
        for i in range(1,word_count+1):
            x=f'Какое то слово № -{i}'
            file.write(x+'\n')
            time.sleep(0.1)
            print(f'Завершилась запись в файл {file_name}')


'''start=time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end=time.time()
print(f'Разница-{end-start}')'''
'''start1=time.time() 
thread1=threading.Thread(target=write_words,args=(10, 'example5.txt'))
thread2=threading.Thread(target=write_words,args=(30, 'example6.txt'))
thread3=threading.Thread(target=write_words,args=(50, 'example7.txt'),daemon=True)
thread4=threading.Thread(target=write_words,args=(40, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread4.join()
end1=time.time()
print(f'Разница-{end1-start1}')'''


'''1. Задача на параллельное выполнение нескольких функций
Условие: Напишите программу, которая выполняет две функции в отдельных потоках. Одна функция будет имитировать долгую задачу (например, sleep(3)),
 а другая — выводить текущее время каждую секунду. После выполнения обеих задач, программа должна завершиться.

Подсказка: Используйте threading.Thread для выполнения этих функций параллельно.

'''

'''def func1():
    x=time.time()
    print(f'{func1.__name__} завершена - {x}')


def func2():
    time.sleep(3)
    x=time.time()
    print(f'{func2.__name__} завершена - {x}')

tread1=threading.Thread(target=func1,args=())
tread2=threading.Thread(target=func2,args=())
tread1.start()
tread2.start()
tread1.join()
tread2.join()'''

'''Задача с использованием start()
Условие: Напишите программу, в которой один поток будет выводить на экран числа от 1 до 5, а второй поток — от 6 до 10. Потоки должны запускаться одновременно.

Описание:

Напишите две функции: одна будет выводить числа от 1 до 5, а другая — от 6 до 10.
Запустите оба потока с помощью метода start().'''

'''def func():
    for i in range(1,17):
        print(i)
def func1():
    for i in range(6,13):
        print(i)
tread1=threading.Thread(target=func,args=())
tread2=threading.Thread(target=func1,args=())
tread1.start()
tread2.start()
tread2.join()'''

'''Условие: Напишите программу, которая запускает три потока, каждый из которых выполняет задачу (например, печатает своё имя). 
Основной поток должен ждать завершения всех потоков с помощью join().

Описание:

Создайте три потока, каждый из которых будет выводить имя потока.
Основной поток должен дождаться завершения всех потоков с помощью join().
Подсказка: Используйте join() в основном потоке, чтобы он ждал завершения всех потоков перед тем, как вывести сообщение о завершении.'''

def func(x):
    print(f'{x}-поток')
tread1=threading.Thread(target=func,args=('Ksenia',)) 
tread2=threading.Thread(target=func,args=('Ivan',))  
tread1.start()
tread2.start()
tread1.join()
tread2.join()
print('Stop')

'''Условие: Напишите программу, которая запускает два потока. Каждый поток должен спать 2 секунды. Основной поток должен выводить, жив ли каждый поток в процессе их выполнения.

Описание:

Создайте два потока, каждый из которых будет выполнять sleep(2).
Основной поток должен проверять, жив ли каждый поток, используя метод is_alive().
Подсказка: Используйте is_alive() для проверки состояния каждого потока в процессе их выполнения.'''

def func(name,x):
    print('start')
    time.sleep(x)
    print('end')

tread1=threading.Thread(target=func,args=(1,1)) 
tread2=threading.Thread(target=func,args=(2,2)) 
tread1.start()
tread2.start()
while tread2.is_alive() or tread1.is_alive():
    print(f'1 жив-{tread1.is_alive()},2 жив-{tread2.is_alive()}')
    time.sleep(0.2)
print('stop')    
'''Условие: Напишите программу, которая запускает два потока. Один поток должен работать в фоновом режиме (как daemon), 
а другой — в обычном режиме. Ожидайте завершения обоих потоков.

Описание:

Создайте два потока: один будет работать как daemon, а другой — обычным потоком.
Используйте daemon=True для создания daemon-потока.
Основной поток должен ждать завершения обоих потоков.
Подсказка: Используйте daemon=True при создании потока для того, чтобы он был фоновым.'''


'''def fun():
    print('start')
    time.sleep(5)
    print('end')
def func1():
    time.sleep(1)
    print('tr tr tr')

tread1=threading.Thread(target=fun,args=())
tread2=threading.Thread(target=func1,args=(),daemon=True)
print('start -osnova')
tread1.start()
tread2.start()

tread2.join()
print('end-osnova')'''
'''Условие: Напишите программу, которая запускает три потока. 
Каждый поток будет выполнять свою задачу (например, выводить своё имя и засыпать на 1 секунду). 
Основной поток должен сначала запустить все потоки, потом дождаться их завершения и проверить, жив ли какой-либо из потоков.

Описание:

Запустите три потока.
После запуска дождитесь их завершения через join().
После этого с помощью is_alive() проверьте, жив ли какой-либо поток.
Подсказка: Используйте is_alive() после того, как потоки завершат выполнение с помощью join().'''

