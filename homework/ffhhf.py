'''1. Глобальная переменная внутри функции: Создайте глобальную переменную и вызовите ее внутри функции.  
'''
f = 1
def x1():
    return f

print(x1())

'''Локальные переменные: Напишите функцию, которая объявляет локальную переменную и возвращает ее значение.
'''

def x2():
    f1 = 2
    return f1

print(x2())

'''3. Использование ключевого слова `global`: Напишите функцию, которая изменяет глобальную переменную внутри функции.  
'''
f3 = 3
def x3():
    global f3
    f3 = 6
    return f3

print(x3())

'''Объявите глобальную и локальную переменные с одинаковыми именами. Какое значение будет возвращено при вызове функции?
'''    

f4 = 6
def x4():
    f4= 7
    return(f4)

print(x4()) # Локальную 

'''Область видимости в цикле и функции: Исследуйте, как работает пространство имен внутри цикла и функции. '''

f5 = []
f6=[1,2,3,5]
def x5():
    for i in f6:
        f5.append(i)
    return f5

print(x5())

'''Использование ключевого слова `nonlocal`: Напишите функцию с вложенной функцией, которая изменяет переменную внешней функции с помощью nonlocal.

'''

def x6():
    f7 = 8
    def x7():
        nonlocal f7
        f7 = 9
    x7()    
    return f7
    
print(x6())    

'''Создайте функцию с одним параметром по умолчанию и вызовите ее без аргументов. '''

def x7(a = 6):
    return a

print(x7())

'''Функция с несколькими параметрами по умолчанию: Напишите функцию с двумя параметрами по умолчанию и вызовите ее, передав только одно значение.
 '''

def x8(a=8,v=7):
    return a,v

print(x8(6))

'''Переопределение параметра по умолчанию: Создайте функцию с параметром по умолчанию и вызовите ее с новым значением для этого параметра. '''

def x9(a=10):
    return a

print(x9(a=6))

'''Изменяемый тип данных в параметре по умолчанию: Используйте список в качестве параметра по умолчанию, измените его внутри функции, и посмотрите, как это повлияет на дальнейшие вызовы.
'''

def x10(a = []):
    x = a.append(10)
    print(x)
    return x

print(x10([1,2,3]))

'''Функция с параметрами по умолчанию и произвольным числом аргументов: Напишите функцию, использующую параметры по умолчанию и произвольное количество позиционных аргументов.  
'''

def x11(a=1,b=2,*args):
    return a,b,args

print(x11(1,6,7,8))

'''Комбинирование параметров по умолчанию и рекурсии: Напишите рекурсивную функцию с параметрами по умолчанию и проанализируйте ее поведение.
'''

def x12(b=10):
    if b ==0:
        return 0
    else:
        return b - x12(b-1)
    
print(x12())  

'''Простая распаковка списка: Напишите функцию, которая принимает два аргумента, и передайте ей список из двух элементов, используя распаковку.  
'''

def x13(a,b):
    return a,b

print(x13(*[1,2]))

'''Распаковка словаря с именованными параметрами: Создайте функцию с двумя именованными параметрами и передайте ей словарь с соответствующими ключами через **.

'''

def x13(a=1,b=2):
    return a,b

aa= {'a':10,'b':10}
print(x13(**aa))

'''**Комбинированная распаковка списка и словаря**: Напишите функцию, принимающую как позиционные, так и именованные аргументы, распаковывая одновременно список и словарь.  
'''

def x14(v,a=10):
    return a,v

print(x14([1,2],{'ff':10}))

'''Распаковка с параметрами по умолчанию: Создайте функцию, которая использует параметры по умолчанию и принимает произвольное количество позиционных и именованных аргументов.
'''

def x16(a=10,*args,**kwargs):
    return a,args,kwargs

print(x16([1,2,3],1,{'dd':10},10))

'''Рекурсивная распаковка аргументов: Напишите рекурсивную функцию, которая принимает и распаковывает произвольное количество аргументов на каждом шаге рекурсии.  
'''
def recursive_unpack(*args):
    # Если нет аргументов, завершить рекурсию
    if not args:
        return
    # Печатаем первый аргумент
    print(args[0])
    # Рекурсивно вызываем функцию с остальными аргументами
    recursive_unpack(*args[1:])

# Пример вызова
recursive_unpack(1, 2, 3, 4, 5)



'''Распаковка и изменение аргументов внутри функции: Напишите функцию, которая распаковывает список и изменяет его элементы внутри функции.

'''

def x17(v:list):
    v.append(10)
    v.append(12)
    v.pop(1)
    v.pop(2)
    return v

print(x17([1,2,2]))

'''Факториал через рекурсию: Напишите рекурсивную функцию для вычисления факториала числа.
'''

def x18(b=10):
    if b ==1:
        return 1
    else:
        return b * x18(b-1)
    
print(x18())  

'''Числа Фибоначчи через рекурсию: Напишите функцию, которая вычисляет число Фибоначчи через рекурсию.'''
def fibonacci(n):
    # Базовые случаи: для n=0 и n=1 возвращаем n
    if n <= 1:
        return n
    # Рекурсивный вызов функции для n-1 и n-2
    return fibonacci(n - 1) + fibonacci(n - 2)

# Пример вызова
print(fibonacci(10))
inv = {}
def add_item(item: str, quantity: int):
    if item in inv:
        inv[item] += quantity
        print(inv)
    else:
        inv[item] = quantity
        print(inv)

add_item("Яблоки",50)
add_item("Яблоки",50)
add_item("Яблоки",50)
add_item("Я",50)
add_item("Я",50)