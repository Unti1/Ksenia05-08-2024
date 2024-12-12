'''### Лёгкие задачи

1. +  **Создание простого класса**  
   Напиши класс `Rectangle` с атрибутами `width` и `height`. Создай объект и выведи его атрибуты.

2. + **Метод для вычисления площади**  
   Добавь метод `area()` в класс `Rectangle`, который вычисляет площадь прямоугольника. Создай объект и вызови метод.

3. + **Метод для установки значений атрибутов**  
   В классе `Rectangle` добавь метод `set_dimensions(width, height)`, чтобы изменять значения ширины и высоты. Проверь работу метода.

4. + **Статический метод для проверки формы**  
   Добавь статический метод `is_square(width, height)` в класс `Rectangle`, который возвращает `True`, если прямоугольник является квадратом.'''

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width    
    
    def set_dimensions(self,width, height):
        self.width = width
        self.height = height

    def is_square(self):
        if self.width == self.height:
            return True    
        return False    

a = Rectangle(20,29)     
print(a.width)
print(a.height)   
print(a.area())
a.set_dimensions(10,29)
print(a.width)
print(a.height) 
a.is_square()
print(a.is_square())

'''5. **Создание класса с предопределённым атрибутом**  
   Напиши класс `Planet` с атрибутом `gravity` по умолчанию равным `9.8`. Создай объект и проверь значение атрибута.
   +-
   '''
class Planet:
    def __init__(self,gravity = 9.8):
        self.gravity = gravity

x = Planet()
print(x.gravity)  

'''6. **Удаление объекта**  
   Создай класс `File` с методом `delete()`, который выводит сообщение: "Файл удалён". Создай объект, вызови метод и удали объект с помощью `del`.
+-   
'''

class File:
    def __del__(self):
        return 'Файл удален!'
    
a = File()
del a 

'''7. **Простая проверка ввода данных**  
   Создай класс `Validator` с методом `is_positive(number)`, который проверяет, является ли число положительным.
   +
   '''
class Validator:
    def is_positive(self,number):
        if number >= 0:
            return "+"
        return "-"

a = Validator()
print(a.is_positive(-1))    


'''8. **Метод с форматированным выводом**  
   Напиши класс `Greeting`, где метод `hello(name)` возвращает строку: "Привет, {name}!".
+
'''
class Greeting:
    def hello(self,name):
        return f'Hello, {name}'
    
a = Greeting()
print(a.hello('dd'))

'''9. **Сравнение объектов по атрибутам**  
   Создай класс `Circle` с атрибутом `radius`. Реализуй метод `compare(circle)` для сравнения радиусов двух объектов и возврата большего радиуса.
   +
   '''
class Circle:
    def __init__(self,radius):
        self.radius = int(radius)

    def __lt__(self, other:int):
        if isinstance(other,Circle):
            if self.radius > other.radius:
                return self.radius
            return other.radius
  
a = Circle(10)
a1 = Circle(200)
print(a.__lt__(a1))  

'''10. + **Класс с фиксированным списком значений**  
    Напиши класс `WeekDays`, который содержит атрибут `days` (список дней недели). Реализуй метод `get_day(index)` для возврата дня недели по индексу.'''
class WeekDays:
    def __init__(self,days:list):
        self.days = days

    def get_day(self,index):
        return self.days[index]


a = WeekDays(['sggs','fgfg','dhd'])
print(a.get_day(2))

'''11. + **Объединение данных объектов**  
    Напиши класс `Notebook` с атрибутом `notes` (список строк). Добавь метод `merge(notebook)`, который объединяет записи из другого объекта в текущий.'''
class Notebook:
    def __init__(self, notes:list):
        self.notes = notes


    def merge(self, other):
        if isinstance(other, Notebook):
            self.notes.extend(other.notes)
            return self.notes
            
            
z = Notebook(['dhhd','dhd'])
z1 = Notebook(['ddd','dhhd'])
print(z.merge(z1))   


'''12. +- **Класс для работы с паролями**  
    Создай класс `PasswordGenerator` с методом `generate(length)`, который генерирует строку заданной длины из случайных символов.'''
import random
from string import ascii_letters

class PasswordGenerator:
    def generate(self,length):
        if length <= 0:
            return "Длина пароля должна быть больше нуля."
        
        # Символы для генерации пароля: буквы, цифры, специальные символы
        password = ''.join(random.choices(ascii_letters, k=length))
        return password
    
a = PasswordGenerator()
print(a.generate(2))
  

'''13. - **Создание объекта на основе данных**  
    Напиши класс `User`, который создаёт объект из строки формата `"Имя: Возраст"`. Реализуй метод `from_string(data)`.'''
class User:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def aa(self, data: str):
        self.name,self.age = data.split(':')  
        return int(self.age), self.name  
    
    @classmethod
    def from_string(cls, data):
        input_args = data.split(':')
        if len(input_args) == 2:
            return cls(*input_args)
         

# a = User()
# print(a.aa('Rcty:20'))
a = User.from_string('Rcty:20')
print(a)



'''14. +- **Подсчёт слов в тексте**  
    Создай класс `WordCounter` с атрибутом `text`. Реализуй метод `count_words()`, который возвращает количество слов в тексте.'''
class WordCounter:
    def __init__(self,text):
        self.text = text

    def __len__(self):
        return len(self.text.split())
    
a = WordCounter('jsj sjj sjs dd') 
print(len(a)) 

'''15. + **Сортировка данных объекта**  
    Создай класс `NumberList` с атрибутом `numbers`. Добавь метод `sort_numbers()`, который сортирует список чисел по возрастанию.'''
class NumberList:
    def __init__(self,numbers:list):
        self.numbers = numbers

    def sort_numbers(self):
        return sorted(self.numbers)
    
a = NumberList([10,22,14])
print(a.sort_numbers())

'''16. +- **Работа с диапазонами чисел**  
    Напиши класс `RangeSum` с методом `sum_in_range(start, end)`, который возвращает сумму всех чисел в указанном диапазоне.
'''
class RangeSum:
    def sum_in_range(self,start, end):
        summ = 0
        for i in range(start,end+1):
            summ += i 
        return summ
a = RangeSum()
print(a.sum_in_range(1,4))    

'''### Сложные задачи

17. + **Управление очередью**  
    Напиши класс `Queue`, который имеет методы `add(item)` для добавления элемента и `remove()` для извлечения первого элемента. Реализуй обработку пустой очереди.'''
class Queue:
    def __init__(self):
        self.list = []
        
    def add(self,x):
        self.list.append(x)
        return self.list
    
    def pop(self):
        if self.list:
            self.list.pop(0)
            return self.list
        return 'Пусто'
    
a = Queue()
print(a.add('ss')) 
print(a.add('ssff')) 
print(a.pop()) 
print(a.pop()) 
print(a.pop())  

'''18. +- **Подсчёт уникальных значений**  
    Создай класс `UniqueCounter` с атрибутом `items`. Реализуй метод `count_unique()`, который возвращает количество уникальных элементов в списке.'''
class UniqueCounter:
    def __init__(self,*items):
        self.items = items


    def count_unique(self):
        return len(set(self.items))    
a = UniqueCounter(10,22,2,22,2)  
print(a.count_unique())  

'''19. - **Перевод валют**  
    Напиши класс `CurrencyConverter` с методом `convert(amount, rate)`, который пересчитывает сумму по заданному курсу и округляет результат до двух знаков.'''
class CurrencyConverter:
    # def __init__(self,sums):
        # self.sums = sums

    def convert(self, amount, rate):
        b = amount * rate    
        return "{:.2f}".format(b)
    
a = CurrencyConverter()    
print(a.convert(29, 120.99))

'''20. +- **Класс с ограничением на добавление данных**  
    Создай класс `LimitedList` с атрибутом `max_length` и методом `add(item)`, который добавляет элемент, но ограничивает длину списка указанным числом. Если список переполнен, удаляется самый старый элемент.'''
class LimitedList:
    def __init__(self,max_length):
        self.spis = []
        self.max_length = max_length 

    def add(self,item):
        if len(self.spis) < self.max_length:
            self.spis.append(item)
            return self.spis
        else:
            self.spis.remove(self.spis[0])
            self.spis.append(item)
        return 'no'

s = LimitedList(2)
print(s.add(20))
print(s.add(20))
print(s.add(20))
print(s.add(20))

'''+ *1 Класс для расчёта среднего арифметического**  
   Напиши класс `AverageCalculator` с методом `add_number(number)` для добавления числа и методом `get_average()`, который возвращает среднее значение добавленных чисел.
'''
class AverageCalculator:
    x = []
    def add_number(self,number):
        return AverageCalculator.x.append(number)
        # return self.__class__.x.append(number)
    
    def get_average(self):
        a = sum(AverageCalculator.x)/len(AverageCalculator.x)
        return a
    
x1 = AverageCalculator()
x1.add_number(1)  
x1.add_number(2)
print(x1.get_average()) 

'''**2 + Класс для работы с датами**  
   Создай класс `DateHandler` с атрибутом `date` (строка в формате "ДД-ММ-ГГГГ"). Реализуй метод `get_year()`, возвращающий год из строки.
'''
class DateHandler:
    def __init__(self,date:str):
        self.date = date

    def get_year(self):
        a = self.date.split('-')
        return a[-1]  
    
a = DateHandler("11-04-1999") 
print(a.get_year())


''' * 3 Создание объекта на основе данных  
   Напиши класс `Book`, который создаёт объект на основе словаря с ключами `"title"` и `"author"`. Добавь метод `from_dict(data)` для инициализации объекта из словаря.

'''

class Book:
    def __init__(self, title, author, **kwargs):
        title = title
        author = author

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


'''+ *4 Проверка уникальности данных**  
   Создай класс `UniqueList` с атрибутом `items` (список). Добавь метод `add(item)`, который добавляет элемент в список, если его там ещё нет.
'''        

class UniqueList:
    def __init__(self,items=[]):
        self.items = items
        
    def add(self,item):
        if item not in self.items:
            self.items.append(item)
            return self.items
        return "Уже есть"   

a = UniqueList()
print(a.add(10))
print(a.add(20))
print(a.add(10))

'''+ **5 Работа с координатами точки**  
   Напиши класс `Point` с атрибутами `x` и `y`. Добавь метод `distance_to(other_point)`, который вычисляет расстояние между текущей точкой и другой.
'''
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance_to(self,other_point):
        if isinstance(other_point,Point):
            x = self.x - other_point.x
            y = self.y - other_point.y
            return math.sqrt(x**2+y**2)
        
a = Point(1,2)
a1 = Point(3,4)
print(a.distance_to(a1))   

'''+ **6 Создание класса для подсчёта символов**  
   Напиши класс `CharCounter` с атрибутом `text`. Добавь метод `count(char)`, который возвращает количество вхождений символа `char` в текст.

'''

class CharCounter:
    def __init__(self,text):
        self.text = text

    def count(self,char):
        return self.text.lower().count(char.lower())
    
a = CharCounter('Ппривет Привет')
print(a.count('П'))    

'''*7 *Генерация последовательности**  
   Напиши класс `SequenceGenerator` с методом `generate(start, step, count)`, который возвращает список из `count` чисел, начиная с `start` и с шагом `step`.

'''
class SequenceGenerator:
    def generate(self, start, step, count):
        result = []
        c = 0
        result.append(start) 
        while c < count:
            c += 1
            start += step
            result.append(start)
        return result
    
s = SequenceGenerator()
print(s.generate(1,2,5))

'''- **8 Класс для работы с инвентарём**  
   Создай класс `Inventory` с атрибутом `items` (словарь, где ключ — название предмета, а значение — количество). Реализуй методы `add_item(name, quantity)` и `remove_item(name, quantity)`'''

class Inventory:
    def __init__(self,items:dict):
        self.items = items

    def add_item(self,name, quantity):
        # self.items.setdefault(name,quantity) # Добавляет но только единажды когда объекта в словаре нет
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        return self.items
    
    def remove_item(self,name, quantity):
        if name in self.items and quantity < self.items[name]:
            self.items[name] -= quantity
        elif name in self.items and quantity == self.items[name]:
            self.items.pop(name)
        else:
            print('Нет столько заданного предмета в инвентаре')
        return self.items
    
x = Inventory({'Chear':10,'Table':2})  
print(x.add_item('sofa',10))
print(x.remove_item('sofa',10))

'''9 + Фильтрация списка по длине строки**  
   Напиши класс `StringFilter` с атрибутом `strings`. Реализуй метод `filter_by_length(length)`, который возвращает строки, длина которых больше заданной.
'''

class StringFilter:

    def __init__(self,string=[]):
        self.strings = string
        
    def filter_by_length(self,length:int):
        for string in self.strings:
            return [string for string in self.strings if len(string) > length] 
                
            
            
        
a = StringFilter(['Ghohh.ssssh.ss','sssss','sss'])
print(a.filter_by_length(2))      

''' + 10 Создай класс `Calculator` с атрибутами `a` и `b`. Добавь метод `sum()`, который возвращает их сумму, и метод `multiply()`, который возвращает их произведение.
'''

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def sum(self):
        return self.a + self.b
    
    def multiply(self):
        return self.a * self.b
a = Calculator(2,4)
print(a.sum())    
print(a.multiply())   

'''**11 Управление сессией пользователя**  
    Создай класс `Session`, который сохраняет имя пользователя и время создания. Добавь метод `is_active(current_time, timeout)`, который проверяет, активна ли сессия, исходя из времени и таймаута.
'''

class Session:
    def __init__(self,name,time):
        self.name =name
        self.time=time

    def is_active(self,current_time, timeout):
        all = timeout +self.time 
        if current_time <= all:
            return 'activ'

a = Session('karl',10)
print(a.is_active(1,1))
'''+ **12 Класс с ограниченным диапазоном значений**  
    Создай класс `BoundedNumber` с атрибутом `value` и методами `increase()` и `decrease()`, которые изменяют значение. Установи ограничения: значение не может быть меньше 0 или больше 100.

'''
class BoundedNumber:
    def __init__(self,value):
        self.value = value
    def increase(self,x):
        if 0 < self.value < 100:
            x1 = self.value + x
            return x1
            
    def decrease(self,y):
        if 0 < self.value < 100:
            y1 = self.value - y
            return y1
    
            
        

x = BoundedNumber(20)
print(x.increase(2)) 
print(x.increase(200)) 
print(x.decrease(3))

'''**13 Работа с матрицей**  
    Напиши класс `Matrix` с атрибутом `data` (двумерный список). Добавь метод `transpose()`, который возвращает транспонированную матрицу.

'''        
'''**14 Создание числовой статистики**  
    Напиши класс `NumberStats` с атрибутом `numbers` (список). Реализуй методы `min()`, `max()` и `mean()`, которые возвращают минимальное, максимальное и среднее значение списка.
'''   

import statistics

class NumberStats:
    def __init__(self,numbers):
        self.numbers = numbers

    def min(self):
        return min(self.numbers)   
    def max(self):
        return max(self.numbers)  

    def mean(self):
        return statistics.mean(self.numbers)  
    
a = NumberStats([1,2,3,4])    
print(a.min())
print(a.max())
print(a.mean())

'''**15 Управление задачами с дедлайном**  
    Создай класс `Task` с атрибутами `name` и `deadline` (строка). Добавь метод `is_overdue(current_date)`, который проверяет, просрочена ли задача.'''

class Task:
    def __init__(self,name,deadline:str):
        self.name = name
        self.deadline= int(deadline)

    def is_overdue(self,current_date):
        if current_date < self.deadline:
            return "No"
        return "Просрочена"

a = Task('X','10')
print(a.is_overdue(20))

'''**16 Класс для форматирования строк**  
    Напиши класс `StringFormatter` с методом `capitalize_words(text)`, который возвращает строку, где каждое слово начинается с заглавной буквы.'''

class StringFormatter:
    def capitalize_words(self,text):
        if text ==  text.capitalize():
            return text

a = StringFormatter()
print(a.capitalize_words('Ghhh'))  


class A:
    def action(self):
        super().action()
        print("Action from A")
        
        
        

class B:
    def action(self):
        print("Action from B")
        

class C(A, B):
    pass

c = C()
c1=A()

c.action()

class A:
    def __init__(self):
        self.a=[]
    def xx(self,other):
        x1=[]
        for x in other.a:
            x1.append(x)
            print(f'+ {x}')
        other.a=x1    
        return other.a    
        
            

            


    

class B(A):
    def set(self,x):
        self.a.append(x)
        return self.a
    
    

x10 = B()
x10.set(10)
x1 = B()
x10.set(11)
x2 = B()



print(x1.xx(x10))


       



























   


















