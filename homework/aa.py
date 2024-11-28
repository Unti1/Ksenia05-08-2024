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












   


















