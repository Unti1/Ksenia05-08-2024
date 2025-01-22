'''Цель: закрепить знания о списочных и словарных сборках, решив несколько небольших задач.

Задача:
Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из списка first_strings 
должно сравниваться с каждым из second_strings. (два цикла)
В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки. Значения строк будут перебираться 
из объединённых вместе списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.

Пример результата выполнения программы:
Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)
Вывод на консоль:
[10, 8, 8]
[('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
{'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}

Примечания:
Помните, когда вы используете 2 цикла for внутри сборки, первый цикл - внешний, второй - внутренний.

Файл module_9_2.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!'''

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first= [len(x) for x in first_strings if len(x)>5]
print(first)
second = [(x,y) for x in first_strings for y in second_strings if len(x)==len(y)]
print(second)
third_results = first_strings +second_strings
print(third_results)
third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}
print(third_result)
'''first_strings = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
second_strings = ['Grape', 'Honeydew', 'Fig', 'Kiwi', 'Lemon']
Создайте список, состоящий из строк из first_strings, где длина строки больше 5.
Создайте список кортежей, где первый элемент — это строка из first_strings, а второй элемент — это строка из second_strings той же длины.
Создайте словарь, где ключ — строка из объединённых списков first_strings и second_strings, а значение — количество гласных в этой строке.'''

first_strings = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
second_strings = ['Grape', 'Honeydew', 'Fig', 'Kiwi', 'Lemon']

first_stringss = [x for x in first_strings if len(x)>5]
print(first_stringss)
second_stringss= [(x,y) for x in first_strings for y in second_strings if len(x)==len(y)]
print(second_stringss)

def x(string):
    vowels = 'aeiouyAYEIOU'
    return sum(1 for x in string if x in vowels)

third={string:x(string) for string in first_strings+second_strings}
print(third)
'''words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'carrot', 'avocado']
Создайте словарь, где ключ — первая буква строки, а значение — список всех слов, начинающихся с этой буквы.
Создайте список всех строк, длина которых кратна 3.
Создайте кортеж, где первый элемент — количество слов, начинающихся на букву "a", а второй элемент — их общая длина.'''
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'carrot', 'avocado']  
def x(word):
    return [xx for xx in words if word.lower()[0]==xx.lower()[0]]
one={x1[0]:x(x1) for x1 in words }
print(one)
two = [x for x in words if len(x)==6]
print(two)
y=0
three= [x for x in words if x[0]=='a']
print(three)
three1=sum(len(x) for x in words if x[0]=='a')
print((len(three),three1))

'''Задача 3: "Группировка по чётности"
Описание: Напишите программу, которая:

Делит список чисел на две группы: чётные и нечётные.
Создаёт словарь, где ключом является чётность числа (True для чётных, False для нечётных), а значением — список чисел этой группы.
Генерирует новый список, где к каждому числу применяется функция:
def custom_transform(x):
    return x ** 2 if x % 2 == 0 else x ** 3'''
def custom_transform(x):
    return x ** 2 if x % 2 == 0 else x ** 3
spic=[1,2,3,4,5,6,7]
x=[custom_transform(x)for x in spic]
print(x)
xx=[(True,x1) if x1%2==0 else (False,x1) for x1 in x]
print(xx)
y=[]
y1=[]       
[y1.append(x[1]) if x[0] == False else y.append(x[1]) for x in xx]
res={'False':y1,'True':y}
print(res)
class Iter:
    def __init__(self,n):
        self.n=n
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>self.i:
            x=self.i
            self.i+=1
            return x
        else:
            raise StopIteration
        
first_n_elements = Iter(5) 

print([x for x in first_n_elements])
def first_n_elements(iterable, n):
    iterator = iter(iterable)  # Создаем итератор из переданного объекта
    result = []  # Список для хранения первых n элементов
    
    for _ in range(n):  # Выполняем n раз
        try:
            result.append(next(iterator))  # Добавляем следующий элемент в список
        except StopIteration:
            break  # Останавливаемся, если итерируемый объект закончился
    
    return result  # Возвращаем список
print(first_n_elements(range(10), 5))







