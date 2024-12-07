'''### **Средний уровень (10 задач)**

1. (+) **Классическая структура классов**
   Создайте класс `Animal` с методом `make_sound`, который возвращает строку `"Some sound"`. Унаследуйте от него классы `Dog` и `Cat`, и переопределите метод так, чтобы он возвращал `"Bark"` и `"Meow"` соответственно. Создайте объекты всех трех классов и вызовите их методы.'''

class Animal:
    def make_sound(self):
        return "Some sound"
class Dog(Animal):
    def make_sound(self):
        return "Bark"
class Cat(Animal):
    def make_sound(self):
        return "Meow"
a=Animal()
print(a.make_sound())    
a1=Dog()
print(a1.make_sound())    
a2=Cat()
print(a2.make_sound())      

'''2. (+) **Атрибуты и инкапсуляция**
   Реализуйте класс `BankAccount` с защищенными атрибутами `_balance` и методом `get_balance`. Добавьте метод `deposit`, который увеличивает `_balance`, и метод `withdraw`, который уменьшает `_balance`, если средств достаточно. Проверьте доступ к `_balance` вне класса.'''
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self,x):
        if x >=0:
            self.__balance +=x
            print(f'Баланс увеличен на {x}')
        else:
            print('Ведите положтельное число') 
    
    def withdraw(self,x):
        if x>=0:
            if x<=self.__balance:
                self.__balance-=x
                print(f'Баланс уменьшен на {x}')
            else:
                print('Недостаточно денег')
        else:
            print('Введите положительное число') 

user = BankAccount(200)
user.deposit(20)  
user.withdraw(30)
print(user.get_balance())

'''3. (+) **Множественное наследование**
   Создайте два базовых класса: `Flyable` с методом `fly` и `Swimmable` с методом `swim`. Унаследуйте от них класс `Duck`, который может как летать, так и плавать. Напишите тестовый код для проверки обоих методов.'''

class Flyable:
    def fly(self):
        print('I can fly!')
class Swimmable:
    def swim(self):
        print('I can swim!')

class Duck(Flyable,Swimmable):
    pass

duck = Duck()
duck.fly()
duck.swim()




'''4. (-) **Перегрузка методов**
   Напишите класс `Calculator` с методом `calculate`, который принимает два числа и знак операции (`+`, `-`, `*`, `/`). Унаследуйте класс `AdvancedCalculator`, добавив поддержку операций `**` и `%`.'''
import math
class Calculator:
    def calculate(self,x,y):
        self.__eq__()

                
    
    def __eq__(self):
        pass




'''5. (+) **Полиморфизм в действиях**
   Создайте классы `Rectangle` и `Circle` с методом `area`, который рассчитывает площадь соответствующей фигуры. Напишите функцию, которая принимает список объектов и вызывает их метод `area`.'''
import math
class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        x = (self.radius**2)*3.14
        return x

def func(y):
    for x in y:
        print(x.area()) 
r = Rectangle(10,19)
c=Circle(10)
x=[r,c]
func(x)        

        
    

'''6. (+) **Доступ к методам через базовый класс**
   Реализуйте базовый класс `Shape` с методом `draw`. Унаследуйте его в классе `Square` и переопределите метод, чтобы он выводил `"Drawing a square"`. Проверьте вызов метода `draw` через базовый класс.'''

class Shape:
    def draw(self):
        pass
class Square(Shape):
    def draw(self):
        print("Drawing a square") 
a = Square()
a.draw()
print(a.draw())        


'''7. (+) **Инкапсуляция с использованием свойств**
   Создайте класс `Person` с приватным атрибутом `__age`. Используйте свойства `getter` и `setter`, чтобы получить и установить возраст только при условии, что он больше 0.'''

class Person:
    def __init__(self):
        self.__age = 0

    def set(self,age):
        if age >0:
            self.__age = age
    def get(self):
        return self.__age   
user = Person()
user.set(40)
print(user.get())



'''8. (+) **Абстрактные классы**
   Создайте абстрактный класс `Employee` с абстрактным методом `calculate_salary`. Реализуйте два подкласса `FullTimeEmployee` и `PartTimeEmployee`, чтобы определить собственные способы расчета зарплаты.'''

class Employee:
    def calculate_salary(self,hour,stavka=120):
        x = hour * stavka
        print(x)
class FullTimeEmployee(Employee):
    def calculate_salary(self,hour,stavka):
        Employee.calculate_salary(hour,stavka)

        
class PartTimeEmployee(Employee):
    def calculate_salary(self,hour):

        Employee.calculate_salary(self,hour)
user1 = FullTimeEmployee()
user2 = PartTimeEmployee()
user1.calculate_salary(20,20)
user2.calculate_salary(20)       



'''9. (+) **Классовые методы и наследование**
   Реализуйте класс `Vehicle` с классовым методом `vehicle_type`, который возвращает `"General vehicle"`. Унаследуйте класс `Car`, который переопределяет этот метод, возвращая `"Car"`.'''

class Vehicle:
    def vehicle_type(self):
        return "General vehicle" 
class Car(Vehicle):
    def vehicle_type(self):
        return "Car"
car = Car()
print(car.vehicle_type())       

'''10. (+) **Динамическая обработка методов**
    Создайте базовый класс `Logger` с методом `log`. Унаследуйте его в классах `ConsoleLogger` и `FileLogger`, которые выводят сообщения на консоль и записывают их в файл соответственно. Напишите функцию, принимающую объект `Logger` и вызывающую метод `log`.'''

class Logger:
    def log(self):
        pass
class ConsoleLogger(Logger):
    x=[]
    def log(self,sms):
        print(sms)
        ConsoleLogger.x.append(sms)
   
class FileLogger(Logger):
    x=[]
    def log(self,sms):
        print(sms)
        FileLogger.x.append(sms)
def func1(logger):
    for x in logger:
        x.log('dhhd')
a1=ConsoleLogger()
a2=FileLogger()
x= [a1,a2]
func1(x)     

### **Высокий уровень (5 задач)**

'''1. (+) **Сложная иерархия классов**
   Разработайте классы `Vehicle`, `Car`, `Truck` и `Motorcycle` с общим базовым классом `Vehicle`. Добавьте общие методы в базовый класс и переопределите их в каждом из подклассов. Используйте полиморфизм для обработки списка объектов, представляющих различные транспортные средства.'''
class Vehicle:
    def pr(self,x):
        print(x)
class Car(Vehicle):
    def pr(self):
        x = "Vr Vr"
        Vehicle.pr(self,x)
class Truck(Vehicle):
    def pr(self):
        x = "Vrrr Vrrr"
        Vehicle.pr(self,x)
class Motorcycle(Vehicle):
    def pr(self):
        x = "Vrrrrrrrr Vr"
        Vehicle.pr(self,x)                
a = Car() 
a1=Truck()
a2 = Motorcycle()
a1.pr()
a2.pr()
a.pr()




'''2. (+) **Инкапсуляция с контролем**
   Создайте класс `Student` с приватными атрибутами `__name` и `__grade`. Реализуйте методы для изменения имени только строкой, а оценки — числом от 0 до 100. Обработайте ошибки ввода данных.'''

class Student:
    def __init__(self,name,grade):
        self.__name = name
        self.__grade = grade
    def set1(self,x):
        if isinstance(x,str):
            self.__name = x
    def set2(self,x):
        if 0<x<100:
            self.__grade =x
    def get(self):
        return self.__grade,self.__name
a = Student('ann',10)
a.set1('hh')
a.set2(20)
print(a.get())            



'''3. (+) **Комплексное множественное наследование**
   Создайте классы `Worker`, `Manager` и `Intern`. `Worker` имеет метод `work`, а `Manager` — метод `manage`. Создайте класс `ProjectManager`, который наследует от обоих классов, добавляя свой метод `plan`.'''

class Worker:
    def work(self):
        pass
class Intern:
    pass
class Manager:
    def manage(self):
        pass
class ProjectManager(Worker,Manager):
    def plan(self):
        pass    

'''4. **Использование метаклассов**
   Реализуйте метакласс, который автоматически добавляет метод `describe` в любой класс, созданный с этим метаклассом. Метод должен возвращать имена всех методов и атрибутов класса.'''



'''5. **Полиморфизм и динамическое создание**
   Напишите функцию, которая принимает название класса как строку и динамически создает объект этого класса. Проверьте работу функции на нескольких классах, реализующих общий метод `describe`.'''


''' **Классическая структура классов**
   Создайте класс `Animal` с методом `make_sound`, который возвращает строку ``. Унаследуйте от него классы `Dog` и `Cat`, и переопределите метод так, чтобы он возвращал `"Bark"` и `"Meow"` соответственно. Создайте объекты всех трех классов и вызовите их методы.'''

class Animal:
    def make_sound(self):
        return "Some sound"
class Dog(Animal):
    def make_sound(self):
        return "Bark"
class Cat(Animal):
    def make_sound(self):
        return "Meow"
an =Animal()
cat=Cat()
dog = Dog()
print(an.make_sound(),cat.make_sound(),dog.make_sound())    
