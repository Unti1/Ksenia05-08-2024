'''Напишите программу, которая выводит каждый символ строки "Привет" на отдельной строке, используя цикл `while`.'''
n = "Привет!"
i = 0
while i < len(n):
    print(n[i])
    i += 1

'''Выведите числа от 1 до 10 с помощью цикла `while`.'''   

x = 0
while x < 11:
    print(x)
    x +=1

'''У вас есть список `[1, 2, 3, 4, 5]`. Выведите его элементы с помощью `while`.''' 

x = [1, 2, 3, 4, 5]
i = 0
while i < len(x):
    print(x[i])
    i += 1

'''Напишите программу, которая выводит числа от 1 до 20, но для четных чисел печатает "Четное", используя цикл `while`.'''   

x = 0
while x <21:
    if x %2 == 0:
        print(f'Четное {x}')
    else:
        print(x)  
    x +=1 

'''Cоздайте строку "python" и выведите её в обратном порядке с помощью `while`.'''         

x ="python" 
i = 0
while i < len(x):
    print(x[::-1])
    break
'''Выведите сумму всех чисел от 1 до 100, используя цикл `while`.'''

x = 0
while x <101:
    print(x)
    x +=1

'''Coздайте список `['a', 'b', 'c']` и выведите элементы списка с индексами с помощью `while`.'''    

x = ['a', 'b', 'c']
i = 0
while i < len(x):
    print( f'{i}-{x[i]}')
    i +=1

'''Напишите программу, которая выводит "Нечетное" для нечетных чисел от 1 до 15 с помощью `while`.'''

x = 0
while x <16:
    if x%2!=0:
        print(f'Нечетное {x}')
    else:
        print(x)   
    x +=1

"""Выведите каждую букву в строке "Код" в верхнем регистре, используя цикл `while`. - НЕ СДЕЛАЛА """     

x = "Код"
i = 0
while i < len(x):
    print(x[i].upper())
    i +=1

'''Напишите программу, которая выводит все кратные 3 числа от 1 до 30 с помощью `while`.'''

x = 0
while x <31:
    if x %3==0:
        print(x)
    x +=1    

'''У вас есть список `[10, 20, 30, 40, 50]`. Создайте новый список, в который будут добавлены элементы, увеличенные на 5, используя `while`.'''  

x =[10, 20, 30, 40, 50]
x1 = []
i = 0

while i < len(x):
    x1.append( x[i]+5 )  #  
    i+=1
print(f'{x1=}')

'''Напишите программу, которая выводит все числа от 1 до 50, делящиеся на 5, с помощью цикла `while`.'''    

x = 0
while x <51:
    if x%5 == 0:
        print(x)
    x +=1    

'''Создайте строку "Hello, World!" и посчитайте количество гласных в этой строке с помощью `while`.'''  

x = "Hello, World!"
i = 0
c = 0
glas = "aeiou"
while i < len(x):
    if x[i].lower() in glas:
        c += 1 
    i +=1  
print(f'{c=}')


'''Выведите таблицу умножения на 7 (от 1 до 10) с помощью цикла `while`.'''

x = 0
while x <8:
    print( f'{x}*7={x*7}')
    x +=1

'''Создайте список из 10 случайных чисел и найдите их среднее значение, используя `while`.'''

x = [1,4,5,9,8,9,4,1,8]
i = 0
while i < len(x):
    i = sum(x)/len(x)
    print((i))
    i +=1
    break

'''Напишите программу, которая проверяет, являются ли числа от 1 до 30 четными или нечетными, и печатает "Четное" или "Нечетное" с помощью `while`.'''
x = 0
while x <31:
    if x %2 ==0:
        print(f'Четное: {x}')
    else:
        print(f'Нечетное: {x}')  
    x +=1

'''Напишите программу, которая считает, сколько раз буква "а" встречается в строке "Алан, давай поиграем", используя `while`.'''    

stroka = "Алан, давай поиграем"
count= 0
i = 0
while i < len(stroka):
    if stroka[i].lower() == 'а':
        count +=1 
    i +=1    
print(f'{count=}')

'''Задача "Нули ничто, отрицание недопустимо!":
Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).
'''
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходный список
ind = 0

while ind < len(my_list) and my_list[ind] >= 0:
    if my_list[ind] != 0:
         print(my_list[ind])
    ind += 1


'''ind = 0
while True:
    if ind > len(my_list):
        break
    if my_list[ind] < 0:
        break
    if my_list[ind] == 0:
        ind += 1
        continue
    print(my_list[ind])
    ind += 1'''





