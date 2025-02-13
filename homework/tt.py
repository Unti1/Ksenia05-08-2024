'''Создай файл `numbers.txt` и запиши в него числа от 1 до 100 через запятую. Затем прочитай файл, найди сумму этих чисел и выведи результат на экран.'''

with open('homework/numbers.txt','r',encoding='utf-8') as file:
    a=file.read().split()
    x=list(map(int,a))
    print(sum(x))
'''Обратный порядок строк**
Считай строки из файла `input.txt` и запиши их в новый файл `output.txt` в обратном порядке (последняя строка станет первой).'''  

with open('homework/input.txt','r',encoding='utf-8') as file:
    a=file.readlines()[::-1]
    x=''.join(a)
    print(x)
with open('homework/output.txt','w',encoding='utf-8') as file:
    file.write(x)


'''Статистика текста
Напиши программу, которая читает текст из файла `text.txt` и выводит:
- количество символов,
- количество слов,
- количество строк.'''

with open('homework/text.txt','r',encoding='utf-8') as file:
    print(len(file.read().split()))
    print(file.tell())
    file.seek(0)
    count=0
    for x in file:
        count+=1
    print(count)  
'''Создай программу, которая ищет слово в файле `data.txt`. Если слово найдено, программа выводит строку, в которой оно есть.
'''   
def func(word):  
    with open('homework/data.txt','r',encoding='utf-8') as file:
        y= file.read().lower().split()
        print(y)
        for x in y:
            if x==word:
                print(x)
                break
                
'''Считай текст из файла `original.txt`. Замени все вхождения слова **"Hello"** на **"Hi"** и запиши результат в новый файл `updated.txt`.'''
with open('homework/original.txt','r',encoding='utf-8') as file: 
    r=file.read().replace('Hello','Hi').split()
    x=','.join(r)
with open('updated.txt','w',encoding='utf-8') as file: 
    file.write(x)
'''Создай файл `user_data.txt` и предложи пользователю ввести 5 строк. Запиши их в файл.''' 
x=[]
def func1():
    global x
    y=input('')
    x.append(y)

y=' '.join(x)
with open('user_data.txt','w',encoding='utf-8') as file: 
    file.write(y)
'''Считай текст из файла `input.txt`, убери все пустые строки и запиши результат в `cleaned.txt`.
'''
with open('homework/input.txt','r',encoding='utf-8') as file: 
    x1=file.read().split()
    x='\n'.join(x1)
with open('homework/cleaned.txt','w',encoding='utf-8') as file:
    file.write(x) 
'''Считай строки из файла `strings.txt`. Для каждой строки проверь, является ли она палиндромом, и запиши результаты в `results.txt`.'''    
with open('homework/strings.txt','r',encoding='utf-8') as file: 
    y=file.read().lower().split('\n')
    for x in y:
        x1=x.replace(' ','')
        if x1==x1[::-1]:
            print(x)
'''Считай текст из `words.txt`, выдели все уникальные слова и запиши их в файл `unique_words.txt`.'''   
with open('homework/words.txt','r',encoding='utf-8') as file: 
    x=set(file.read().lower().split())
    x=' '.join(x)
    print(x)
with open('homework/unique_words.txt','w',encoding='utf-8') as file:    
    file.write(x)

'''Создай программу, которая читает данные о студентах (имя и оценка) из файла `students.txt` и форматирует их так:  
**"Имя: Иван, Оценка: 5"**  
Запиши отформатированные данные в файл `formatted_students.txt`.'''
with open('homework/students.txt','r',encoding='utf-8') as file: 
    with open('homework/newstudents.txt','w',encoding='utf-8') as filee:     
        for x in file:
            x1,y=x.split()
            z=f'Имя:{x1:>6}, Оценка:{y:<6}\n'
            print(z)
            filee.write(z)
'''Создай файл `numbers.txt`, содержащий случайные числа. Напиши программу, которая:
1. Копирует числа из файла,
2. Сортирует их по возрастанию,
3. Записывает отсортированные числа в файл `sorted_numbers.txt`.'''   
with open('homework/numbers.txt','r',encoding='utf-8') as file:  
    x=file.read().split()
    x=list(map(int,x))
    x.sort()
    print(x)
    x=list(map(str,x))
    x='\n'.join(x)
    print(x)
'''Создай несколько файлов `file1.txt`, `file2.txt` и `file3.txt`. Объедини их содержимое в один файл `merged.txt`.'''
with open('homework/file1.txt','r',encoding='utf-8') as file1:  
    with open('homework/file2.txt','r',encoding='utf-8') as file2:  
        with open('homework/file3.txt','r',encoding='utf-8') as file3:  

            x=[]
            x+=file1.read().split()
            x+=file2.read().split()
            x+=file3.read().split()
            x=','.join(x)
            print(x)
'''Есть файл `logs.txt`, где каждая строка — это запись вида:  
`[ERROR] Ошибка на сервере 12:34:56`  
Считай файл и посчитай количество ошибок и предупреждений в нем. Выведи результат на экран.
'''
with open('homework/logs.txt','r',encoding='utf-8') as file:  
    x1=file.read().split('\n')
    count1=0
    count2=0
    for x in x1:
        if '[WARNING]' in x:
            count1+=1
        elif '[ERROR]' in x:
            count2+=1
print(count2,count1)   
'''Создай программу, которая считывает текстовый файл `input.txt` и удаляет все пробелы и пустые строки, сохраняя результат в `compressed.txt`.
.
'''
with open('homework/input.txt','r',encoding='utf-8') as file:  
    with open('homework/compressed.txt','w',encoding='utf-8') as file1: 
        x=file.read().split()
        x='\n'.join(x)
        print(x)
        file1.write(x)
'''Класс для работы с файлами**
Создай класс `FileHandler`, который инкапсулирует методы для:
- чтения из файла,
- записи в файл,
- добавления новых данных.

Протестируй класс на файле `data.txt`.'''   

class FileHandler:
    def __init__(self,name):
        self._name=name
    def read(self):
        with open(self._name,'r',encoding='utf-8') as file: 
            print(file.read())
    def write(self,*x): 
        x=list(map(str,x))
        x=' '.join(x)
        with open(self._name,'w',encoding='utf-8') as file: 
            file.write(x+'\n')
    def append(self,*x):  
        x=list(map(str,x))
        x=' '.join(x)
        with open(self._name,'a',encoding='utf-8') as file: 
            file.write(x+'\n')       

a=FileHandler('homework/data.txt')
a.write(['ssss','ssss'])
a.append('h')
a.read()
'''Напиши программу, которая создает файл `program_log.txt` и сохраняет в нем записи о времени запуска программы и выполненных действиях.'''
from datetime import datetime

def time(x):
    with open('homework/program_log.txt','w',encoding='utf-8') as file: 
        now = datetime.now()  
        fnow=now.strftime('%H:%M')
        file.write(f'{fnow}:{x}')
time('f')    
        
'''Напиши программу, которая создает текстовые файлы `file1.txt`, `file2.txt` и т.д. Запакуй их в архив (zip) с помощью Python.'''
with open('homework/file1.txt','r',encoding='utf-8') as file: 
    with open('homework/file2.txt','r',encoding='utf-8') as file1: 
        x=file.read().split()
        x1=file1.read().split()
        x3=list(zip(x,x1))
        print(x3)




           

