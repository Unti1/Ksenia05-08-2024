'''Напишите функцию высшего порядка, которая принимает другую функцию и число, а затем возвращает результат применения этой функции к числу. '''
def func(x,y):
    return x(y)
def func1(x):
    return x *2

print(func(func1,3))

'''Используйте функцию map, чтобы возвести каждый элемент списка [1, 2, 3, 4, 5] в квадрат.
'''
x=[1, 2, 3, 4, 5]
def func(x):
    return x**2
x=list(map(func,x))
print(x)

''' filter: Используйте функцию filter, чтобы из списка [10, 15, 20, 25, 30] оставить только числа, которые делятся на 5 без остатка.
'''
def func(x):
    if x %5==0:
        return True
        
    
x1=[10, 15, 20, 26, 30]   
x1=filter(func,x1)
print(list(x1))

'''Списковые сборки: Создайте список квадратов чисел от 1 до 10 с помощью списочного выражения.
'''
x=[x**2 for x in range(1,11)]
print(x)

'''Словарные сборки: Создайте словарь, где ключи — числа от 1 до 5, а значения — их кубы.
'''
x={x:x**3 for x in range(1,6)}
print(x)
''' Итераторы: Используйте встроенный итератор range, чтобы вывести числа от 1 до 5.'''

for x in range(1,6):
    print(x)

'''Генераторы: Напишите простую функцию-генератор, которая возвращает числа от 1 до 5.

'''    

def func():
    for r in range(1,6):
        yield r

print(list(func()))

'''Декораторы: Напишите простой декоратор, который выводит сообщение до и после выполнения функции.
'''

def func(func):
    def wrapper():
        x=func()
        print('Start','\n',x,'\n','End')
    return wrapper

@func
def func1():
    return 1

func1()
'''map и filter: Используйте map и filter вместе, чтобы из списка [1, 2, 3, 4, 5] оставить только чётные числа и возвести их в квадрат.

'''
def func(x):
    if x%2==0:
        return True
def func1(x):
    return x**2
xx = [1, 2, 3, 4, 5]
x=map(func1,filter(func,xx))
print(list(x))
        
'''yield: Напишите функцию-генератор, которая возвращает первые n чисел Фибоначчи.
'''
'''Функции высшего порядка: Напишите функцию, которая принимает другую функцию и два числа, а затем возвращает результат применения переданной функции к этим числам.
'''

def func(x,y,z):
    return x(y),x(z)
def func1(x):
    return x+2

print(func(func1,1,4))
'''12. filter: Из списка слов ["apple", "banana", "cherry", "date"] оставьте только те, которые содержат букву 'a', используя filter.
'''
def a(x):
    if 'a' in x:
        return True
xx=["apple", "banana", "cherry", "date"]    
xx=filter(a,xx)  
print(list(xx))  
'''Словарные сборки: Создайте словарь, где ключи — это строки из списка ["a", "b", "c"], а значения — их ASCII-коды.

'''
x=["a", "b", "c"] 
xx={x:ascii(x) for x in x}
print(xx)
'''Создание итератора: Реализуйте собственный класс итератора, который возвращает квадраты чисел от 1 до заданного предела.
'''
class Iterator:
    def __init__(self,end):
        self.end=end
        self.step=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.step < self.end:
            x= self.step
            self.step+=1
            return x
        raise StopIteration
        
        

a=Iterator(10)  
for x in a:
    print(x)

'''Функции-генераторы: Напишите генератор, который возвращает бесконечную последовательность чётных чисел.
'''
def decor1():
    x = 0  
    while True:
        if x % 2 == 0:  
            yield x  
        x += 1  

a = decor1()  
for _ in range(10): 
    print(next(a))
      
'''Сложный декоратор: Напишите декоратор, который измеряет время выполнения функции.

'''
import time
def timedec(func):
    def wrapper(*args,**kwargs):
        start= time.time()
        print(func(*args,**kwargs))
        end=time.time()
        return f'начало-{start},конец-{end}'
    return wrapper    

@timedec
def func():
    return 1+2

print(func())


''' map: Используйте функцию map для конкатенации строк из двух списков: ["a", "b", "c"] и ["1", "2", "3"].

'''
def func(x,y):
    return x+y
x= ["a", "b", "c"]
x1=["1", "2", "3"]
z= map(func,x,x1)
print(list(z))
    
'''Комбинирование генераторов: Создайте два генератора: один для чисел, другой для их квадратов. Используйте их вместе для создания пар (число, квадрат).

'''
def genn1(x):
    for xx in x:
        yield xx
def genn2(x):
    for xx in x:
        yield xx**2
x=[1,2,3,4]    
x1=genn1(x)
x2=genn2(x)
for x,y in zip(x1,x2):
    print(x,y)
   

'''Функции высшего порядка: Напишите функцию высшего порядка, которая принимает список функций и список значений, применяет каждую функцию ко всем значениям и возвращает результат в виде вложенного списка.

'''
def func1(x):
    return x*2
def func2(x):
    return x**2

def func(x,y):
    x= [list(map(xx,y)) for xx in x]
    return x
print(func([func1,func2],[1,2,3]))    
''' Итераторы: Реализуйте итератор, который возвращает числа из последовательности Фибоначчи до заданного предела.

'''  


'''Функции-генераторы: Напишите генератор, который принимает список чисел и возвращает только уникальные числа, сохраняя порядок их появления.

'''
def xxx(numbers):
    xx=set()
    for x in numbers:
        if x not in xx:
            yield x
            xx.add(x)

x12=xxx([1,2,3,1,8,9,0,1])
for x in x12:
    print(x)
'''Трёхуровневый декоратор: Напишите декоратор с параметром, который принимает текст сообщения. Декоратор должен выводить это сообщение перед выполнением функции.
'''

def decorr(x):
    def deccc(func):
        def wrapper():
            xx=func()
            print(x)
            return xx
        return wrapper
    return deccc

@decorr('jj')
def s():
    return '10'

print(s())

'''Комбинированные инструменты: Используйте списковые сборки, функции map, filter и декоратор, чтобы обработать список строк ["123", "abc", "456", "def"], оставив только числовые строки и преобразовав их в числа.

'''
# подсмотрела any
def k(x):
    return not any(y in x for y in "abcdef")
def decorator(func):
    def wrapper(x):
        x=map(int,filter(k,func(x)))
        return list(x)
    return wrapper 
        
@decorator
def func00(x):
    return x

print(func00(["123", "abc", "456", "def"]))
  
'''Сложные генераторы: Реализуйте генератор, который возвращает бесконечную последовательность простых чисел.

'''

def gen11(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def gen12():
    x=0
    while True:
        if gen11(x):
            yield x
        x+=1
gen = gen12()
for _ in range(10):
    print(next(gen))
'''Оптимизация производительности: Напишите декоратор, который кэширует результаты выполнения функции для ускорения повторных вызовов.'''


