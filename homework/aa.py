'''### Лёгкие задачи

1. **Создание простого класса**  
   Напиши класс `Rectangle` с атрибутами `width` и `height`. Создай объект и выведи его атрибуты.

2. **Метод для вычисления площади**  
   Добавь метод `area()` в класс `Rectangle`, который вычисляет площадь прямоугольника. Создай объект и вызови метод.

3. **Метод для установки значений атрибутов**  
   В классе `Rectangle` добавь метод `set_dimensions(width, height)`, чтобы изменять значения ширины и высоты. Проверь работу метода.

4. **Статический метод для проверки формы**  
   Добавь статический метод `is_square(width, height)` в класс `Rectangle`, который возвращает `True`, если прямоугольник является квадратом.

5. **Создание класса с предопределённым атрибутом**  
   Напиши класс `Planet` с атрибутом `gravity` по умолчанию равным `9.8`. Создай объект и проверь значение атрибута.

6. **Удаление объекта**  
   Создай класс `File` с методом `delete()`, который выводит сообщение: "Файл удалён". Создай объект, вызови метод и удали объект с помощью `del`.

7. **Простая проверка ввода данных**  
   Создай класс `Validator` с методом `is_positive(number)`, который проверяет, является ли число положительным.

8. **Метод с форматированным выводом**  
   Напиши класс `Greeting`, где метод `hello(name)` возвращает строку: "Привет, {name}!".

'''

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

class Planet:
    def __init__(self,gravity = 9.8):
        self.gravity = gravity

x = Planet()
print(x.gravity)  

class File:
    def __dell__(self):
        return 'Файл удален!'
    
a = File()
print(a.__dell__())    


class Validator:
    def is_positive(self,number):
        if number >= 0:
            return "+"
        return "-"

a = Validator()
print(a.is_positive(-1))    

class Greeting:
    def hello(self,name):
        return f'Hello, {name}'
    
a = Greeting()
print(a.hello('dd'))

'''9. **Сравнение объектов по атрибутам**  
   Создай класс `Circle` с атрибутом `radius`. Реализуй метод `compare(circle)` для сравнения радиусов двух объектов и возврата большего радиуса.

10. **Класс с фиксированным списком значений**  
    Напиши класс `WeekDays`, который содержит атрибут `days` (список дней недели). Реализуй метод `get_day(index)` для возврата дня недели по индексу.

11. **Объединение данных объектов**  
    Напиши класс `Notebook` с атрибутом `notes` (список строк). Добавь метод `merge(notebook)`, который объединяет записи из другого объекта в текущий.

12. **Класс для работы с паролями**  
    Создай класс `PasswordGenerator` с методом `generate(length)`, который генерирует строку заданной длины из случайных символов.

13. **Создание объекта на основе данных**  
    Напиши класс `User`, который создаёт объект из строки формата `"Имя: Возраст"`. Реализуй метод `from_string(data)`.

14. **Подсчёт слов в тексте**  
    Создай класс `WordCounter` с атрибутом `text`. Реализуй метод `count_words()`, который возвращает количество слов в тексте.

15. **Сортировка данных объекта**  
    Создай класс `NumberList` с атрибутом `numbers`. Добавь метод `sort_numbers()`, который сортирует список чисел по возрастанию.

16. **Работа с диапазонами чисел**  
    Напиши класс `RangeSum` с методом `sum_in_range(start, end)`, который возвращает сумму всех чисел в указанном диапазоне.
'''

class Circle:
    def __init__(self,radius):
        self.radius = int(radius)

    def __lt__(self,other:int):
        if isinstance(other,Circle):
            if self.radius > other.radius:
                return {self.radius}
            return 
  
        
    
a = Circle(10)
a1 = Circle(20)
print(a.__lt__(9))    

class WeekDays:
    def __init__(self,days:list):
        self.days = days

    def get_day(self,index):
        return self.days[index]


a = WeekDays(['sggs','fgfg','dhd'])
print(a.get_day(2))

class Notebook:
    def __init__(self,notes):
        self.notes = notes


    def merge(self,other):
        if isinstance(other,Notebook):
            b = self.notes + other.notes
            return b
        
z = Notebook(['dhhd','dhd'])
print(z.merge(['ssj','dd']))   

class WordCounter:
    def __init__(self,text):
        self.text = len(text)
    

    def __len__(self):
        return self.text
    
a = WordCounter('jsjsjjsjs') 
print(a.__len__())   

class NumberList:
    def __init__(self,numbers:list):
        self.numbers = str(numbers)

    def sort_numbers(self):
        return self.numbers
    
a = NumberList([10,22,34])
print(a.sort_numbers)

class RangeSum:
    def sum_in_range(self,start, end):
        














