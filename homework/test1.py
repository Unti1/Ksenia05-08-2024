'''Задачи к сегодняшнему зачёту:

1. Создание класса  
   Создай класс Person с атрибутом name. Создай объект этого класса и выведи значение атрибута name.'''

class Person:
    def __init__(self,name,age,city):
        self.name =  name
        self.age = age
        self.city = city
        # print (f'Hi {self.name}, your from {self.city}, you are {self.age}')
    def greet(self):
        print (f'Hi {self.name}, your from {self.city}, you are {self.age}')
    def birthday(self):
        self.age +=1  
    def __str__(self):
        return f'Hi {self.name}, your from {str(self.city)}, you are {self.age}'




ksenia = Person("Ksenia",22,'ekb')
ksenia.greet()
print(ksenia.age)
ksenia.birthday()
print(ksenia.age)
print(ksenia)

class Wallet:
    def __init__(self,balance):
        self.balance = balance

    def __add__(self,other):
        return Wallet(self.balance +other.balance)
    

a1= Wallet(10)
a2 = Wallet(20000)
b = a1 +a2
print(b.balance)

class Dog:
    species = 0
    
    def __init__(self,name,age):
        self.name = name 
        self.age  = age


Bob = Dog("Bov",22) 

print(Dog.species)

class Libraly:
    all = 0
    
    def __init__(self,name,book):
        self.name = name
        self.book = book
        Libraly.all += self.book
        

    def library_info(self):
        return f"В библиотеке сейчас общее колличество книг - {Libraly.all}" 
    
    def book_count(self):
        return f"В {self.name} сейчас {self.book}"
    
    
    
    
a= Libraly("s",20)
a2= Libraly("sg",20)
a3= Libraly("sg",20)

print(a.library_info())
print(a.book_count())
print(a2.library_info())
print(a2.book_count())
print(Libraly.all)





    
'''Атрибуты объекта  
   В классе Person добавь атрибуты age и city. Создай объект с заполненными атрибутами и выведи их значения.

3. Методы объекта  
   Добавь метод greet() в класс Person, чтобы он выводил приветствие с именем человека. Создай объект и вызови этот метод.

4. Инициализатор `__init__`  
   Добавь метод __init__ в Person, чтобы автоматически задавать значения name, age и city при создании объекта. Создай объект с этими параметрами.

5. Указатель на объект (`self`)  
   Добавь метод birthday() в класс Person, который увеличивает значение age на 1 с использованием self. Проверь изменение возраста.

6. Специальный метод `__str__`  
   Добавь метод __str__ в Person, чтобы при вызове print(person) выводились name, age и city. Создай объект и проверь вывод.

7. Перегрузка оператора сложения (`__add__`)  
   Напиши класс Wallet с атрибутом balance. Переопредели метод __add__ для сложения балансов двух объектов Wallet. Создай два объекта и сложи их.

8. Классовый атрибут  
   В классе Dog создай атрибут класса species, общий для всех объектов, и добавь атрибуты экземпляра name и age. Создай объекты и проверь значение species.

9. Метод класса и метод экземпляра  
   Реализуй метод класса library_info() и метод экземпляра book_count() в классе Library. Первый метод должен возвращать общее количество книг, а второй — число книг в конкретной библиотеке.

10. Перегрузка метода `__len__`  
    Создай класс Playlist, который принимает список песен и реализует метод __len__, чтобы возвращать количество песен.'''

class Playlist:
    def __init__(self,spis):
        self.spis = len(spis)

    def __len__(self):
        return self.spis
    
ass = Playlist(('aa','ss'))
print(len(ass))        



'''Метод `__new__` для управления созданием объектов  
    Напиши класс Singleton, использующий __new__, чтобы создавать только один экземпляр этого класса. Проверь поведение при создании нескольких объектов.'''

class Singleton:
    x = None

    def __new__(cls):
        if Singleton.x is None:
            Singleton.x = super().__new__(cls)
        return Singleton.x
    
x1 = Singleton()
x2 = Singleton()
print( x1 is x2)    
        

'''12. Работа с атрибутами класса и экземпляра  
    Создай класс Counter, добавь атрибут класса count для подсчета созданных объектов. Создай несколько объектов и проверь значение count.'''

class Counter:
    count = 0

    def __init__(self):
        Counter.count +=1

x1 = Counter()
x2 = Counter()
x3 =Counter()
print(Counter.count)        

'''13. Регистрация и проверка уникальности  
    Создай класс RegistrationSystem с методом для добавления новых пользователей и проверки уникальности их логинов. Храни пользователей в классовом атрибуте.'''

class RegistrationSystem:
    all = set()

    def __init__(self,name):
        self.name = name
        
        

    def add(self):
        if self.name in RegistrationSystem.all:
            return f'Уже есть'
        else:
            RegistrationSystem.all = self.name
            return f'Добавлен'
    @classmethod
    def user_count(cls):
        
        return f"Общее число зарегистрированных пользователей: {len(cls.all)}"
    
        
        

a = RegistrationSystem('Ева')        
print(a.add())
a2 = RegistrationSystem('Ева')        
print(a2.add())

print(RegistrationSystem.all)
print(RegistrationSystem.user_count())


'''14. Приватные и защищенные атрибуты  
    В классе BankAccount создай защищенный атрибут _balance и приватный атрибут __pin. Реализуй методы для изменения этих атрибутов с проверкой.

15. Декораторы методов класса  
    Добавь в RegistrationSystem декоратор @classmethod для метода, возвращающего общее число зарегистрированных пользователей.

16. Перегрузка оператора сравнения (`__eq__`)  
    Напиши класс Product с атрибутами name и price. Переопредели метод __eq__, чтобы сравнение двух продуктов происходило по имени и цене.'''

class Product:
    def __init__(self,name,prace):
        self.name = name
        self.prace = prace

    def __eq__(self,other):
        if isinstance(other,Product):
            return self.name ==other.name and self.prace == other.prace
        return False

product1 = Product("Laptop", 1500)
product2 = Product("Laptop", 1500)
product3 = Product("Phone", 700)

print(product1 == product2)  # True (одинаковое имя и цена)
print(product1 == product3)         


'''17. Контроль доступа к атрибутам  
    Создай класс ProtectedData с атрибутом data и методами для получения и изменения значения с проверкой. Попробуй напрямую изменить data.'''

class ProtectedData:
    data = 0
    def __init__(self):
        pass

    @classmethod
    def add(cls):
        cls.data +=1
        return cls.data

a = ProtectedData()
print(a.add())
print(a.add())

'''18. Счетчик вызовов метода  
    Создай класс MethodCounter с методом track(), который подсчитывает, сколько раз он был вызван для конкретного объекта.'''

class MethodCounter:
    def __init__(self):
        self.count = 0
    
    
    def track(self):
        self.count +=1
        return self.count

a = MethodCounter()

print(a.track())
print(a.track())




'''19. Управление доступом к атрибуту  
    Напиши класс Temperature, с приватным атрибутом _celsius, и добавь методы get_celsius() и set_celsius(). При установке значения проверь, что температура не выходит за заданные пределы.

20. Система покупки товаров  
    Создай класс ShoppingCart, где можно добавлять и удалять товары с указанием их цены и количества. Реализуй метод для подсчета общей стоимости корзины.'''







'''21. Кэширование результатов метода  
    Создай класс FibonacciCalculator с методом calculate(n), который вычисляет n-е число Фибоначчи. Добавь кэширование, чтобы повторные вызовы с теми же значениями n возвращали закэшированный результат, а не вычисляли его заново.


22. Лог действий пользователя  
    Создай класс UserActivityLogger для логирования действий пользователя. Каждый объект имеет уникальный идентификатор пользователя и метод log_action(action), который записывает действие в атрибут activity_log (список строк). Реализуй метод get_last_n_actions(n), который возвращает последние n действий пользователя.''' 
class UserActivityLogger:
    def __init__(self,id):
        self.id = id
        self.activity_log = []

    def log_action(self,action):
        self.activity_log.append(action)

    def get_last_n_actions(self):
        return self.activity_log[-1] 

x = UserActivityLogger(123)
x.log_action('dhhdhd')
x.log_action('dhdhd')
print(x.get_last_n_actions())
    



'''23. Подсчёт и управление экземплярами с удалением  
    Напиши класс Task, который увеличивает атрибут класса active_tasks при создании экземпляра и уменьшает его при удалении объекта. Реализуй метод __del__, чтобы корректно отслеживать удаление объектов. Также добавь метод get_active_tasks() для получения текущего количества активных задач.'''

class Task:
    count = 0
    def __init__(self):
        Task.count +=1
    def __del__(self):
        Task.count -= 1
    def get_active_tasks(self):
        return Task.count

a = Task()
a1 = Task()
a3 = Task()
print(a.get_active_tasks()) 
a3.__del__()
print(a.get_active_tasks())




  
'''24. Менеджер задач с приоритетом  
    Создай класс TaskManager, который управляет списком задач с приоритетами. Задачи должны храниться в виде словаря, где ключ — приоритет, а значение — список задач с этим приоритетом. Реализуй методы для добавления и удаления задач, а также метод get_next_task(), который возвращает задачу с наивысшим приоритетом и удаляет её из очереди.

25. Управление доступом к атрибутам через декораторы  
    Напиши класс TemperatureControl с приватным атрибутом _temperature и декоратором для метода temperature, который проверяет, что значение температуры устанавливается только в пределах допустимого диапазона (например, от -50 до 150 градусов). Реализуй также метод display_temperature() для вывода текущего значения в градусах Цельсия и Фаренгейта.'''

