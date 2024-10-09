'''### Легкие задачи

1. Напиши функцию, которая принимает два числа и возвращает их сумму.
2. Напиши функцию, которая принимает строку и возвращает её длину.
3. Напиши функцию, которая принимает список чисел и возвращает максимальное значение в списке.
4. Напиши функцию, которая принимает строку и возвращает её в верхнем регистре.
5. Напиши функцию, которая принимает кортеж и возвращает список с теми же элементами.
6. Напиши функцию с опциональным аргументом, которая возвращает удвоенное значение переданного числа, если аргумент не передан — умножает на 3.
7. Напиши функцию, которая принимает строку и символ, и возвращает количество вхождений этого символа в строку.
8. Напиши функцию, которая принимает список строк и возвращает количество строк длиной больше 5 символов.
9. Напиши функцию, которая принимает два словаря и возвращает их объединение.
10. Напиши функцию, которая принимает строку и возвращает её перевёрнутой (используя срезы).

### Средние задачи

11. Напиши функцию, которая принимает строку и возвращает True, если строка является палиндромом, иначе False.
12. Напиши функцию с неограниченным количеством аргументов (*args), которая возвращает их произведение.
13. Напиши функцию, которая принимает список чисел и возвращает новый список, содержащий только чётные числа.
14. Напиши функцию с опциональным аргументом, которая возвращает сумму списка, если аргумент не передан — возвращает длину списка.
15. Напиши функцию, которая принимает строку и заменяет все пробелы на дефисы.
16. Напиши функцию, которая принимает словарь и возвращает список всех его ключей.
17. Напиши функцию, которая принимает два множества и возвращает их пересечение.
18. Напиши функцию, которая принимает список чисел и возвращает True, если список отсортирован по возрастанию.
19. Напиши функцию с неограниченным количеством аргументов (**kwargs), которая принимает имена и возраст людей, и возвращает имя самого молодого.
20. Напиши функцию, которая принимает строку и возвращает новый список, где каждый элемент — это слово из строки.

### Сложные задачи

21. Напиши функцию, которая принимает список чисел и возвращает все возможные комбинации этих чисел.
22. Напиши функцию, которая принимает два списка и возвращает True, если они содержат хотя бы один общий элемент.
23. Напиши функцию, которая принимает строку и возвращает True, если все символы в строке уникальны (используя множество).
24. Напиши функцию, которая принимает список кортежей, каждый кортеж содержит имя и возраст, функция возвращает отсортированный список по возрасту.
25. Напиши функцию, которая принимает список слов и возвращает словарь, где ключ — это слово, а значение — это длина слова.'''

'''Напиши функцию, которая принимает два числа и возвращает их сумму.'''

def sum_of_two(one, two):
    i = one + two
    return i

print(f'1: {sum_of_two(2,3)}')

"""Напиши функцию, которая принимает строку и возвращает её длину."""
def get_len_str(one):
    i = len(one)
    return i

print( f'2: {get_len_str("Какая то строка")}')  

'''Напиши функцию, которая принимает список чисел и возвращает максимальное значение в списке.'''

def max_of_lst(lst, *args):
    print(args)
    return max(lst) 

print('3:',max_of_lst( [1,2,3,4,5,6,7] ) )

"""Напиши функцию, которая принимает строку и возвращает её в верхнем регистре."""
def up(one):
    i = one.upper()
    return i

print('4:', up('нижний'))

'''Напиши функцию, которая принимает кортеж и возвращает список с теми же элементами.'''
def to_list(tup):
    return list(tup)
print('5:',to_list((44,55,66)))

'''Напиши функцию, которая принимает кортеж и возвращает список с теми же элементами.'''
def to_list(k):
    return(list(k))

print('6:', to_list((44,55,66)) ) 

'''Напиши функцию с опциональным аргументом, которая возвращает удвоенное значение переданного числа, 
если аргумент не передан — умножает на 3. НЕ СОВСЕМ ПОНЯЛА'''

def func(x = 0):
    if x:
        return(x*2)
    else:
        return(x*3)    

print('7:', func(7))
print('7:', func())

'''Напиши функцию, которая принимает строку и символ, и возвращает количество вхождений этого символа в строку.'''
def count_of_sym(string: str, sym: str):
    string = string.lower()
    count = string.count(sym)
    return count

print('8:', count_of_sym('Какая то строка', 'к'))

'''Напиши функцию, которая принимает список строк и возвращает количество строк длиной больше 5 символов. '''
def more_then_5_len(k):
    count = 0
    lst = []
    for i in k:
        if len(i) > 5:
            count += 1
            lst.append(i)
    return lst, count

print('9:',more_then_5_len(['eeee','eeeeee','fhfhfhfhfh']))


#TODO: Остальное переделать в том же духе

'''Напиши функцию, которая принимает два словаря и возвращает их объединение.'''
def list1(k:list,d:list):
    k.extend(d)
    return k 
print('10:',list1([1,2,3],[2,3,4,5]))

'''Напиши функцию, которая принимает строку и возвращает её перевёрнутой (используя срезы).'''
def str1(k:str):
   return k[::-1]
print('11:',str1('hi'))

'''Напиши функцию, которая принимает строку и возвращает True, если строка является палиндромом, иначе False.'''
def str2(k:str):
    if k == k[::-1]:
        return True
    else:
        return False
print('12:',str2('non'))      

'''Напиши функцию с неограниченным количеством аргументов (*args), которая возвращает их произведение.'''
def chtoto(*args: int):
    return sum(args)

print('13:',chtoto(12,12))

''' Напиши функцию, которая принимает список чисел и возвращает новый список, содержащий только чётные числа. NO '''
def list2(k: list):
    d =[]
    for i in k:
        if i % 2 ==0:
            d.append(i)
    return d

print('14:',list2([55,22,77,10]))
     
'''14.Напиши функцию с опциональным аргументом, которая возвращает сумму списка, если аргумент не передан — возвращает длину списка.'''
def sum_list3(k=[12,33,44,77]):
    if k==[12,33,44,77]:
        return sum(k)
    else:
        return len(k)
print('15:',sum_list3([12,33])) 

'''Напиши функцию, которая принимает строку и заменяет все пробелы на дефисы.'''

def str4(k:str):
    return k.replace(' ','-')

print('16:',str4('dhd dhdh'))   

'''Напиши функцию, которая принимает словарь и возвращает список всех его ключей.'''

def dict1(**kwargs):
    return kwargs.keys()

print('17:',dict1(n=50, my_arg=[1,2,3])) 

'''Напиши функцию, которая принимает два множества и возвращает их пересечение.'''

def set1(i,b: set):
    return i & b

print('18:',set1({1,2,3}, {2,3,4}))  

'''Напиши функцию, которая принимает список чисел и возвращает True, если список отсортирован по возрастанию. NO'''
def list5(d: list):
    k = d.copy() # если пишем равно, то идет двойное присвоение? 
    k.sort()
    if d == k:
        return True
    else:
        return False
    
print('19:', list5([7,2,3]))
print('19:', list5([2,3,4]))
'''Напиши функцию с неограниченным количеством аргументов (**kwargs), которая принимает имена и возраст людей, и возвращает имя самого молодого.'''
def chtoto2(**kwarg):
    k = min(kwarg, key=kwarg.get)
    return k

print('20:',chtoto2(Ksen=22,Anna=33,Tim=999))

'''Напиши функцию, которая принимает строку и возвращает новый список, где каждый элемент — это слово из строки.'''
def str6(i:str):
    return i.split()

print('21:',str6('shhsshss hshshh ssh'))  
'''Напиши функцию, которая принимает список чисел и возвращает все возможные комбинации этих чисел.'''
import itertools
 
def list9(i:list):
    permutations = list(itertools.permutations(i))

    for p in permutations:
        print(p)
    return p     

print('22:',list9([22,33,44,55]))

'''Напиши функцию, которая принимает два списка и возвращает True, если они содержат хотя бы один общий элемент.'''

def func9(k,k1: list):
    k=set(k)
    k1=set(k1)
    if k & k1:
        return True
    else:
        return False    
print('23:',func9([1,2,33],[66,88]))

'''Напиши функцию, которая принимает строку и возвращает True, если все символы в строке уникальны (используя множество).'''

def func10(l:str):
    k = set(l)
    for i in k:
        count = l.count(i)
        if count <= 1:
            return True 
        else:
            return False       

print('24:',func10('ls'))            

'''24. Напиши функцию, которая принимает список кортежей, каждый кортеж содержит имя и возраст, функция возвращает отсортированный список по возрасту.'''


def func11(k:tuple):
    k = sorted(k, key=lambda student: student[1])
    return k

print('25:',func11([
    ('Anna',44),
    ('Ksen',33),
    ('sjsjs',15)
]))
'''Напиши функцию, которая принимает список слов и возвращает словарь, где ключ — это слово, а значение — это длина слова.'''

def func12(k:list):
    d = []
    l = []
    # dct = {}
    for i in k:
        d = len(i)
        l.append(d)
        j = dict(zip(k, l))

    # for key in k:
    #     dct[key] = len(key)
    return j #, dct
        
print('26:',func12(['ssss','ddd','dddd']))          