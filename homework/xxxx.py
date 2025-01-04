'''...### Легкие задания (5 шт.)

1 +. Проверка делимости.  
   Напишите программу, которая принимает два числа и проверяет, делится ли первое на второе без остатка. Если пользователь ввел некорректные данные или второе число равно нулю, обработайте исключения.'''

def func(x,y):
    try:
        if x % y == 0:
            return True
        else:
            return False
    except ZeroDivisionError:
        print('На ноль делить нельзя')   
    except TypeError:
        print('Неверный формат')     
func(2,2)

'''2 +. Сложение с проверкой.  
   Напишите функцию, которая принимает два аргумента, преобразует их в числа и возвращает их сумму. Если преобразование не удалось, обработайте исключение и выведите сообщение.'''
def func1(x,y):
    try:
        return(int(x)+int(y))
    except ValueError as e:
        print(f'{e}')
print(func1('1','2'))   
'''3 +. Открытие файла на запись.  
   Напишите программу, которая пытается записать данные в файл. Если файл недоступен для записи, обработайте соответствующее исключение.'''

def func2(x):
    try:
        with open(x,'a',encoding='utf-8') as file:
            print(file.write('xx'))
    except FileNotFoundError:
         print('Файл не найден')    

func2('hfhdddddfff.txt')                 
               
          
'''4 +. Модульное деление.  
   Создайте функцию, которая выполняет модульное деление двух чисел. Обработайте ZeroDivisionError и TypeError в случае некорректных данных.'''
def func3(x,y):
    try:
        return x//y
    except ZeroDivisionError:
        print('На ноль делать нельзя')    
    except TypeError:
        print('Неверный формат')    
func3(1,1)        

'''5 +. Чтение элемента множества.  
   Напишите программу, которая принимает строку от пользователя и проверяет, есть ли она в множестве. Если множеству передано не строковое значение, обработайте исключение.'''


def func4(x):
    x1={'1','2','3'}
    try: 
        # for xx in x1:
        #     if xx==x:
        #         print(xx)
        if x in x1:
            return True
        else:
            return False
        
    except TypeError:
        print('Не тот формат')    
func4('1')            


### Средние задания (10 шт.)

'''1 -. Фильтрация списка.  
   Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий только положительные числа. Если элемент списка не является числом, выбрасывайте исключение и обработайте его.'''
def func5(x):
    x1=[]
    for xx in x:
        try:
            if isinstance(xx, (int, float)):
                if xx >= 0:
                    x1.append(int(xx))
            else: 
                raise TypeError(f'{xx} - Неподдерживаемый тип данных')
        except TypeError as e:
            print(e)
    return x1      
print('mid 1: ', func5([1,2,'23', 2, -24, 2, 'sf']))     

'''2 +. Чтение нескольких файлов.  
   Напишите программу, которая открывает и читает несколько файлов, указанных пользователем. Если какой-либо файл отсутствует, обработайте это и продолжите выполнение программы.'''


def func6(*filenames):
    for filename in filenames:
        try:
            with open(filename, 'r', encoding='utf-8') as fl:
                ...
        except FileNotFoundError:
            print(f'Такого файла нет - {filename}')
print('mid 2: ', func6('file.txt', 'words.txt'))     

# def func6(x,y):
#     try:
#         with open(x,'r',encoding='utf-8') as file:
#             with open(y,'r',encoding='utf-8') as file1:
#                 print(file.read())
#                 print(file1.read())
#     except FileNotFoundError:
#         pass



'''3 +. Напишите функцию, которая принимает список и словарь. Функция пытается обратиться к элементу списка по индексу и к ключу в словаре. Обработайте все возможные исключения.'''

def func7(x,y):
    try:
        print(x[1],y['key'])
    except IndexError:
        print('Индекса нет такого') 
    except KeyError:
        print('Ключа нет') 
func7([1,2],{'key1':1})        



'''4 +-. Вызов функции через ввод.  
   Напишите программу, которая принимает от пользователя имя функции и аргументы, а затем вызывает соответствующую функцию. Обработайте исключения, если пользователь указал неверные данные.'''
def func8(x,y):
    try:
        x(y)
    except TypeError:
        print('Не тот формат')        
    except NameError:
        print('Такой функции не существует')
func8(func5, [1,2,'ff'])        


'''6 +. Проверка длины строки.  
   Напишите программу, которая принимает строку и проверяет, чтобы она была не короче 5 символов. Если строка короче, выбрасывайте собственное исключение StringTooShortError.'''

class StringTooShortError(Exception):
    def __init__(self,message='Строка короче 5 симоволов'):
        self.message = message 
        super().__init__(self.message)

def chek(x):
    if len(x)<5:
        raise StringTooShortError
    
def func9(x):
    try:
        chek(x)
        print(x)  
    except StringTooShortError:
        print('Измени')

func9('123555')        

'''7 -. Работа с вложенными словарями.  
   Напишите функцию, которая принимает словарь с вложенными структурами. Попробуйте получить значение из вложенного словаря, обработав KeyError на любом уровне.'''
def func10(x,y):
    try:
        for y1 in y:
            print(x[y1])
    except KeyError as a:
        print(f'Ключ {a} не найден')        
      
func10({"name": "John", "age": 30,"address": {"city": "New York"}},["addres"])  
'''8 +. Конвертация валют.  
   Создайте программу, которая принимает курс валюты и сумму в другой валюте. Обработайте исключения, если пользователь вводит некорректные данные.'''
class Zero(Exception):
    def __init__(self,message='0 нелья'):
        self.message = message 
        super().__init__(self.message)

def chek(value):
    if value==0:
        raise Zero       

def func11(value, curse):
    try:
        chek(value)
        print(value*curse)
    except TypeError:
        print('Неверный формат')   
    except Zero:
        print('0 нельзя')     

func11(20.2,0)

'''10 +. Функция с генерацией исключения.  
    Создайте функцию, которая принимает строку и выбрасывает исключение ValueError, если строка содержит пробел. Обработайте исключение в вызывающем коде.'''

class Probel(Exception):
    def __init__(self,message='убери пробел'):
        self.message = message 
        super().__init__(self.message)

def chek(x):
    if x.count(' '):
        raise Probel      
    
def func12(x):
    try:
        chek(x)
        print(x)
    except TypeError:
        print('Неверный формат')   
    except Probel:
        print('Убери пробел')
func12('аапп')


### Сложные задания (5 шт.)

'''1. Каскадная обработка исключений.  
   Напишите программу, которая последовательно вызывает несколько функций (например, открытие файла, обработка данных, запись в новый файл). Каждая функция выбрасывает свое исключение. Реализуйте каскадную обработку этих исключений в вызывающем коде.'''
def func13(x):
    try:
        with open(x,'r',encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError as a:
        print(f'{a} не найден')   
def func14(x):
    try:
        with open(x,'a',encoding='utf-8') as f:
            f.write('Ксения')
        func13(x)
    except TypeError as a:
        print(f' {a} - формат не тот')      
def func15(x):
    try:
        with open(x,'w',encoding='utf-8') as f:
            f.write('Привет ')
        func14(x)
    except TypeError as a:
        print(f' {a} - 1формат не тот')             


func15('1.txt')
'''2. Создание класса исключения с атрибутами.  
   Напишите собственное исключение InvalidDataError, которое принимает сообщение об ошибке и данные, вызвавшие ошибку. Реализуйте программу, которая выбрасывает это исключение и обрабатывает его.'''
class InvalidDataError(Exception):
    def __init__(self,message='Цифра меньше 8 - ошибочка'):
        self.message=message
        super().__init__(self.message)
def chek(x):
    if x < 8:
        raise InvalidDataError()
    

def func16(x):
    try:
        chek(x)
        print(x)
    except InvalidDataError as a:
        print(a)
func16(6)        
'''5. Генерация ошибок через объект.  
   Создайте класс CustomProcessor, который имеет метод process. Метод выбрасывает исключение, если данные объекта не прошли валидацию. Напишите код для обработки этой ошибки.'''

class Age(Exception):
    def __init__(self,message='Возраст должен быть больше 18'):
        self.message=message
        super().__init__(self.message)



class CustomProcessor():
    def __init__(self,age):
        self.age=age
    def process(self):
        if self.age < 18:
            raise Age()
            
try:
    a=CustomProcessor(8) 
    a.process()
    print('Готово')
except Age as a:
    print(a)    

        