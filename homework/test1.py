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




  
'''1. Автомобиль и его производные  
   Создайте класс Car с инкапсулированными полями brand, model, year и методом get_info, который возвращает информацию об автомобиле. Создайте классы-наследники ElectricCar и GasCar.  
   - В классе ElectricCar добавьте поле battery_capacity и метод get_info, который возвращает информацию о батарее.  
   - В классе GasCar добавьте поле fuel_tank_capacity и переопределите метод get_info для отображения информации о топливном баке.'''
class Car:
    def __init__(self,brand,model,year):
        self.__brand=brand
        self.__model = model
        self.__year = year

    def get_info(self):
        return f'{self.__brand}-brand,{self.__model}-model,{self.__year}-year'
        
class ElectricCar(Car):
    def __init__(self,brand,model,year,batery):
        self.__batery = batery
        Car.__init__(self,brand,model,year)

    def get_info(self):
        return f'{Car.get_info(self)},{self.__batery}-batery' 
class GasCar(Car):
    def __init__(self,brand,model,year,fuel_tank_capacity):
        self.__fuel_tank_capacity = fuel_tank_capacity
        Car.__init__(self,brand,model,year)

    def get_info(self):
        return f'{Car.get_info(self)},{self.__fuel_tank_capacity}-fuel_tank_capacity' 
    
c = Car('bmw','m3',2021)  
print(c.get_info()) 
e = ElectricCar('bmw','m3',2021,'ff')
print(e.get_info())
G = GasCar('bmw','m3',2021,'f87f')
print(G.get_info())





'''2. Фигуры и их площади  
   Создайте базовый класс Shape с методом area, который возвращает NotImplementedError. Создайте классы-наследники Circle, Rectangle и Triangle.  
   - Реализуйте метод area для каждого наследника.  
   - Напишите функцию print_area, которая принимает объект Shape и печатает его площадь.'''
class Shape:
    def area(self):
        raise NotImplementedError
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        x = 3.14 * self.radius **2
        return x

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
def print_area(shape):
    if isinstance(shape,Shape):
        return f'Площадь {shape.area()}'
circle = Circle(5)         
rectangle = Rectangle(4, 6)  
triangle = Triangle(8, 3)  
print(print_area(circle))       
print(print_area(rectangle))      
print(print_area(triangle))     


    
'''3. Банковские счета  
   Создайте класс BankAccount с инкапсулированным полем balance и методами deposit и withdraw. Создайте класс SavingsAccount, который добавляет процентную ставку (interest_rate).  
   - Реализуйте метод для начисления процентов.  
   - Проверьте, что прямой доступ к полю balance невозможен.'''
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposit(self,x):
        if x >= 0:
            self.__balance += x
            print(f'Баланс увеличен на {x} рублей')
        else:
            print('Напишите положительную сумму')    
    def withdraw(self,y):
        if y >=0:
            if y <= self.__balance:
                self.__balance -= y
                print(f'Баланс уменшен на {y} рублей')
            else:
                print(f'На счету недостаточно денег')  
        else:
            print(f'Напишите положительную сумму')        
    def get(self):
        return self.__balance
    def accrual(self,interest_rate):
        x = self.get() % interest_rate
        self.__balance = self.__balance + x
        print(f'Общий баланс с учетом {interest_rate} процентов равен - {self.get()} рублей')

class SavingsAccount(BankAccount):
    def __init__(self,balance,interest_rate):
        self.interest_rate = interest_rate
        BankAccount.__init__(self,balance)
    def accrual(self):
        BankAccount.accrual(self,self.interest_rate) # так ведь можно?

user = SavingsAccount(200,30)
print(user.get())
user.accrual()
user.deposit(200)
print(user.get())
user.withdraw(20)
print(user.get())


        
    

'''4. Животные и их звуки  
   Создайте базовый класс Animal с методом make_sound. Создайте классы Dog и Cat, которые переопределяют метод make_sound. Напишите функцию, которая принимает список объектов Animal и вызывает для каждого метод make_sound.'''
class Animal:
    all =[]
    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self):
        Animal.all.append(self)
    def make_sound(self):
         print('Гав нав')
class Cat(Animal):
    def __init__(self):
        Animal.all.append(self)
    def make_sound(self):
        print('Мяу мяу')
def func(animal):
        for x in animal:
            x.make_sound()
      
ava=Dog()
ava1 = Dog()
mau = Cat() 
x = [ava,ava1,mau]
func(x)



'''5. Чат и пользователи  
   Создайте класс User с методами отправки и получения сообщений. Создайте класс-наследник AdminUser, который может удалять сообщения других пользователей.  
   - Реализуйте логику проверки, может ли пользователь удалять сообщения.  
   - Используйте инкапсуляцию для хранения списка сообщений.'''

class User:
    
    def __init__(self,name):
        self.__all = []
        self.name = name
        
    def send(self,sms,other):
        other.set().append(sms)
        print(f'Вы отправили сообщение "{sms}" пользавателю {other.name}')
    def receiving(self,sms,other):
        self.__all.append(sms) 
        print(f'Вы получили сообщение "{sms}" от пользавателя {other.name}')  
    def set(self):
        return self.__all     
class AdminUser(User):
    def __init__(self):
        pass
    def dell(self,other,sms):
         if sms in other.set():
            other.set().remove(sms)
            print(f'Сообщение "{sms}" удалено у пользавателя {other.name}')
         else: print(f'Сообщение "{sms}" не найдено у пользавателя {other.name}')

user1 = User('Bob')
user2=User('Ann')
user3=User('Dan')
user1.send('Hi,Ann!',user2)
user1.receiving('No',user3)
admin = AdminUser()
admin.dell(user1,'hi')
admin.dell(user2,'Hi,Ann!')

### Сложные задачи

'''6. Система оплаты сотрудников  
   Создайте базовый класс Employee с методами для расчета зарплаты. Создайте классы-наследники HourlyEmployee и SalariedEmployee.  
   - В первом классе зарплата рассчитывается на основе отработанных часов и ставки.  
   - Во втором — фиксированная ставка.  
   - Реализуйте метод для вывода общей суммы зарплат из списка сотрудников.'''

class Employee:
    def zp(self):
        raise NotImplementedError
    
    def zp(self,hour,stavka=10):
        x = hour * stavka
        self.zpall = x
        print(f'Общая зарплата сотрудника {self.zpall}')
        
class HourlyEmployee(Employee):
    def __init__(self):
        self.zpall = 0

    def zp(self,hour:int,stavka:int):
        Employee.zp(self,hour,stavka)
class SalariedEmployee(Employee):
    def __init__(self):
        self.zpall= 0
    def zp(self,hour):
        Employee.zp(self,hour)
        
def alll(employee):
    all = 0
    for x in employee:
        all+=x.zpall
    return  f'Общая зарпата всех сотрудников {all}'

a1=HourlyEmployee()
a2 = SalariedEmployee()
a2.zp(100)
a1.zp(30,200)
a3 = Employee()
x=[a1,a2]
print(alll(x))





'''7. Ролевая игра  
   Создайте базовый класс Character с инкапсулированными полями health и attack_power. Создайте классы Warrior и Mage.  
   - Реализуйте методы для атаки и восстановления здоровья.  
   - Добавьте полиморфный метод special_ability, который будет уникальным для каждого класса.'''

class Character:
    def __init__(self,health,attack_power):
        self.__health=health
        self.__power = attack_power
    def getp(self):
            return self.__power
    def geth(self):
        return self.__health
    def attack(self,other):
        
        x = self.geth() - other.getp() 
        self.__health = x
        return x
    def vostan(self):
        pass
class Warrior(Character):
    pass
class Mage(Character):
    pass

w=Warrior(100,30)
m=Mage(90,50)
print(m.attack(w))



    



class Warrior(Character):
    def __init__(self,health,attack_power):
        Character.__init__(self,health,attack_power)
    
class Mage(Character):
    def __init__(self,health,attack_power):
        Character.__init__(self,health,attack_power)         


'''8. Магазин и товары  
   Создайте базовый класс Product с методами для получения цены и информации о товаре. Создайте классы Electronics, Clothing и Food, которые добавляют свои уникальные атрибуты (например, срок годности для еды).  
   - Реализуйте общий метод для подсчета скидки, который будет работать по-разному в каждом классе.'''
class Product:
    def __init__(self,price,info):
        self._price = price
        self.info = info
    def get(self):
        return f'Цена товара - {self._price}'  

    
class Electronics(Product):
    def __init__(self,price,info,guarantee):
        self.guarantee = guarantee
        Product.__init__(self,price,info)
    def discond(self):
        return f'Wена с учетом скидки 25% - {self._price * 0.25} долларов'


          

a=Electronics(200,'jdjdj',2)
print(a.discond()) 


'''9. Транспортные средства  
   Создайте базовый класс Transport с методами для подсчета времени в пути. Создайте классы-наследники Car, Train и Airplane, которые добавляют свою скорость и особенности.  
   - Реализуйте метод, который принимает список объектов Transport и возвращает объект с минимальным временем в пути.'''
class Transport:
    def __init__(self,distance):
        self._distance= distance
    def get(self):
        return f'общая дистанция {self._distance}'
    def traveltime(self,speed):
        return f'Время за которое объект проедет {self._distance} км - {self._distance / speed} часов'
class Car(Transport):
    def __init__(self,distance,speed,carnew:bool):
        self._distance= distance
        self.speed = speed
        self.carnew = carnew
        Transport.__init__(self,distance)
    def traveltime(self):
        if self.carnew == True:
            return (Transport.traveltime(self,self.speed)) / 2
        else:
            return Transport.traveltime(self,self.speed)
        
a =  Car(200,10,False)   
print(a.traveltime())

'''10. Управление файлами  
    Создайте класс File с методами для записи, чтения и удаления файлов. Создайте классы TextFile и BinaryFile, которые переопределяют методы для работы с текстовыми и бинарными файлами.  
    - Добавьте инкапсулированное поле для хранения пути к файлу.  
    - Реализуйте проверку доступа перед выполнением операций с файлами.'''

    
'''### **Средний уровень (10 задач)**

1. **Классическая структура классов**
   Создайте класс `Animal` с методом `make_sound`, который возвращает строку `"Some sound"`. Унаследуйте от него классы `Dog` и `Cat`, и переопределите метод так, чтобы он возвращал `"Bark"` и `"Meow"` соответственно. Создайте объекты всех трех классов и вызовите их методы.

2. **Атрибуты и инкапсуляция**
   Реализуйте класс `BankAccount` с защищенными атрибутами `_balance` и методом `get_balance`. Добавьте метод `deposit`, который увеличивает `_balance`, и метод `withdraw`, который уменьшает `_balance`, если средств достаточно. Проверьте доступ к `_balance` вне класса.

3. **Множественное наследование**
   Создайте два базовых класса: `Flyable` с методом `fly` и `Swimmable` с методом `swim`. Унаследуйте от них класс `Duck`, который может как летать, так и плавать. Напишите тестовый код для проверки обоих методов.

4. **Перегрузка методов**
   Напишите класс `Calculator` с методом `calculate`, который принимает два числа и знак операции (`+`, `-`, `*`, `/`). Унаследуйте класс `AdvancedCalculator`, добавив поддержку операций `**` и `%`.

5. **Полиморфизм в действиях**
   Создайте классы `Rectangle` и `Circle` с методом `area`, который рассчитывает площадь соответствующей фигуры. Напишите функцию, которая принимает список объектов и вызывает их метод `area`.

6. **Доступ к методам через базовый класс**
   Реализуйте базовый класс `Shape` с методом `draw`. Унаследуйте его в классе `Square` и переопределите метод, чтобы он выводил `"Drawing a square"`. Проверьте вызов метода `draw` через базовый класс.

7. **Инкапсуляция с использованием свойств**
   Создайте класс `Person` с приватным атрибутом `__age`. Используйте свойства `getter` и `setter`, чтобы получить и установить возраст только при условии, что он больше 0.

8. **Абстрактные классы**
   Создайте абстрактный класс `Employee` с абстрактным методом `calculate_salary`. Реализуйте два подкласса `FullTimeEmployee` и `PartTimeEmployee`, чтобы определить собственные способы расчета зарплаты.

9. **Классовые методы и наследование**
   Реализуйте класс `Vehicle` с классовым методом `vehicle_type`, который возвращает `"General vehicle"`. Унаследуйте класс `Car`, который переопределяет этот метод, возвращая `"Car"`.

10. **Динамическая обработка методов**
    Создайте базовый класс `Logger` с методом `log`. Унаследуйте его в классах `ConsoleLogger` и `FileLogger`, которые выводят сообщения на консоль и записывают их в файл соответственно. Напишите функцию, принимающую объект `Logger` и вызывающую метод `log`.

---

### **Высокий уровень (5 задач)**

1. **Сложная иерархия классов**
   Разработайте классы `Vehicle`, `Car`, `Truck` и `Motorcycle` с общим базовым классом `Vehicle`. Добавьте общие методы в базовый класс и переопределите их в каждом из подклассов. Используйте полиморфизм для обработки списка объектов, представляющих различные транспортные средства.

2. **Инкапсуляция с контролем**
   Создайте класс `Student` с приватными атрибутами `__name` и `__grade`. Реализуйте методы для изменения имени только строкой, а оценки — числом от 0 до 100. Обработайте ошибки ввода данных.

3. **Комплексное множественное наследование**
   Создайте классы `Worker`, `Manager` и `Intern`. `Worker` имеет метод `work`, а `Manager` — метод `manage`. Создайте класс `ProjectManager`, который наследует от обоих классов, добавляя свой метод `plan`.

4. **Использование метаклассов**
   Реализуйте метакласс, который автоматически добавляет метод `describe` в любой класс, созданный с этим метаклассом. Метод должен возвращать имена всех методов и атрибутов класса.

5. **Полиморфизм и динамическое создание**
   Напишите функцию, которая принимает название класса как строку и динамически создает объект этого класса. Проверьте работу функции на нескольких классах, реализующих общий метод `describe`.'''

''' **Классическая структура классов**
   Создайте класс `Animal` с методом `make_sound`, который возвращает строку `"Some sound"`. Унаследуйте от него классы `Dog` и `Cat`, и переопределите метод так, чтобы он возвращал `"Bark"` и `"Meow"` соответственно. Создайте объекты всех трех классов и вызовите их методы.'''












