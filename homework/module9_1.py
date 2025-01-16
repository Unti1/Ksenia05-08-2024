'''Домашнее задание по теме "Введение в функциональное программирование"
Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.

Задача "Вызов разом":
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
Эта функция должна:
Вызвать каждую функцию к переданному списку int_list
Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
Пункты задачи:
В функции apply_all_func создайте пустой словарь results.
Переберите все функции из *functions.
При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
Верните словарь results.
Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
Пример результата выполнения программы:
В примере используются следующие функции:
min - принимает список, возвращает минимальное значение из него.
max - принимает список, возвращает максимальное значение из него.
len - принимает список, возвращает кол-во элементов в нём.
sum - принимает список, возвращает сумму его элементов.
sorted - принимает список, возвращает новый отсортированный список на основе переданного.
Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
Вывод на консоль:
{'max': 20, 'min': 6}
{'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
Примечания:
Для того, чтобы взять название функции можно обратиться к атрибуту name
При попытке передачи, например, списка из строк, некоторые функции могут работать некорректно или вовсе не работать. Используйте списки чисел.
Файл module_9_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!'''

def func1(x):
    return x+1
def func2(x):
    return x*2

def apply_all_func(int_list:list[int,float], *functions):
    results={}
    for function in functions:
        try:
            x=list(map(function,int_list))
            results[function.__name__]=x
        except TypeError:
            x=function(int_list)
            results[function.__name__]=x
            
    print(results) 

    
    

apply_all_func([6, 20, 15, 9],func1,func2)
apply_all_func([6, 20, 15, 9], max, min)
apply_all_func([6, 20, 15, 9], len, sum, sorted)

'''Задача 1: "Фильтры на все случаи"
Описание:
Напишите функцию apply_filters(int_list, *filters), которая принимает:

int_list — список чисел (int, float).
*filters — неограниченное количество функций-фильтров, которые возвращают True или False для каждого элемента списка.
Функция должна:

Применить каждую функцию-фильтр к списку и оставить только те элементы, для которых фильтр вернёт True.
Вернуть словарь, где ключом является название функции-фильтра, а значением — отфильтрованный список.'''
def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0
 
def apply_filters(int_list:list[int,float], *filters):
    result={}
    for filterr in filters:
        x=set(list(filter(filterr,int_list)))
        result[filterr.__name__] =x
    print(result)
apply_filters([-1,0,1,2,3,4,0,5,6,7],is_even,is_positive)    
apply_filters([6, -2, 15, -9, 8, 0], is_even, is_positive)

'''Задача 2: "Применение шаг за шагом"
Описание:
Напишите функцию apply_stepwise(int_list, *functions), которая:

Принимает список чисел и несколько функций.
Применяет каждую функцию к результату предыдущей.
Возвращает результат после применения всех функций.
Пример:

def add_one(x):
    return x + 1

def square(x):
    return x ** 2

print(apply_stepwise([1, 2, 3], sum, add_one, square)) '''
def apply_stepwise(int_list, *functions):
    x1=int_list
    for func in functions:
        try:
            x1=list(map(func,x1))
        except TypeError:
            x1=func(x1)    
    print(x1)        

def add_one(x):
    return x + 1

def square(x):
    return x ** 2

apply_stepwise([1, 2, 3], sum,add_one,square)

'''"Каскадная обработка"
Описание:
Напишите функцию cascade_processing(data, *steps), которая принимает:

data — список чисел.
*steps — последовательность функций, которые нужно применять к списку шаг за шагом.
Функция должна:

Передавать результат каждой функции следующей.
Вернуть результат последней функции.
Пример:

def add_one(x):
    return [i + 1 for i in x]

def square(x):
    return [i ** 2 for i in x]

print(cascade_processing([1, 2, 3], add_one, square))  # [4, 9, 16]'''

def cascade_processing(data, *steps):
    x=data
    for step in steps:
        try:
            x=list(map(step,x))
        except TypeError:
            x=step(x)
    print(x)   

def add_one(x):
    return x+1

def square(x):
    return x**2

cascade_processing([1, 2, 3], add_one, square)

'''
Задача 4: "Условное применение функции"
Описание:
Напишите функцию conditional_apply(data, condition, transform), которая принимает:

data — список чисел.
condition — функция, возвращающая True или False для числа.
transform — функция, преобразующая число.
Функция должна:

Применять функцию transform только к тем элементам списка, которые удовлетворяют условию condition.
Вернуть новый список.
Пример:

def is_even(x):
    return x % 2 == 0

def double(x):
    return x * 2

print(conditional_apply([1, 2, 3, 4], is_even, double))  # [1, 4, 3, 8]'''

def is_even(x):
    return x % 2 == 0

def double(x):
    return x * 2

def conditional_apply(data, condition, transform):
    xx=[]
    for x in data:
        if is_even(x):
            x=double(x)
            xx.append(x)
        else: xx.append(x)    
    print(xx)    
conditional_apply([1, 2, 3, 4], is_even, double)

'''Задача 5: "Модульное преобразование"
Описание:
Создайте функцию apply_with_module(int_list, module_func, *functions), которая:

Применяет каждую функцию к списку.
К каждому результату применяет переданную функцию module_func.
Пример:

def abs_list(x):
    return [abs(i) for i in x]

def add_five(x):
    return [i + 5 for i in x]

def sum_elements(x):
    return sum(x)

print(apply_with_module([6, -20, 15, -9], abs_list, add_five, sum_elements))'''

def apply_with_module(int_list, module_func, *functions):
    for func in functions:
        try:
            x=list(map(func,int_list))
            
            x1=list(map(module_func,x))
            print(f'{func.__name__}- {x1}')
        except TypeError:
            x=func(int_list)
            
            x1=module_func(x)
            print(f'{func.__name__}- {x1}')
       
            
        
def abs_list(x):
    return abs(x)

def add_five(x):
    return x+5

def sum_elements(x):
    return sum(x)    

apply_with_module([6, -20, 15, -9], abs_list, add_five, sum_elements)

'''Напишите функцию custom_transform(data, transformer), которая принимает:

data — список чисел.
transformer — функцию, которая преобразует каждое число.
Задача функции:

Преобразовать каждый элемент списка data с помощью функции transformer.
Вернуть преобразованный список.
Пример:

def square(x):
    return x ** 2

def halve(x):
    return x / 2

print(custom_transform([1, 2, 3, 4], square))  # [1, 4, 9, 16]
print(custom_transform([10, 20, 30], halve))  # [5.0, 10.0, 15.0]'''

def custom_transform(data, transformer):
    print(list(map(transformer,data)))
def square(x):
    return x ** 2

def halve(x):
    return x / 2    
    
custom_transform([1, 2, 3, 4], square)
custom_transform([10, 20, 30], halve)

'''"Выбор функции для операции"
Описание:
Напишите функцию choose_operation(numbers, operation), которая принимает:

numbers — список чисел.
operation — строку, определяющую, какую операцию применить (например, "sum", "max", "min").
Функция должна:

В зависимости от значения строки operation вызывать соответствующую встроенную функцию Python (sum, max, min).
Вернуть результат выполнения функции.
Пример:

print(choose_operation([1, 2, 3, 4], "sum"))  # 10
print(choose_operation([1, 2, 3, 4], "max"))  # 4
print(choose_operation([1, 2, 3, 4], "min"))  # 1'''

def choose_operation(numbers, operation):
    if operation == "sum":
        return sum(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    
    
print(choose_operation([1, 2, 3, 4], "sum"))
print(choose_operation([1, 2, 3, 4], "max"))  
print(choose_operation([1, 2, 3, 4], "min"))  

'''Задача 3: "Каскадная обработка"
Описание:
Напишите функцию cascade_processing(data, *steps), которая принимает:

data — список чисел.
*steps — последовательность функций, которые нужно применять к списку шаг за шагом.
Функция должна:

Передавать результат каждой функции следующей.
Вернуть результат последней функции.
'''

def add_one(x):
    return x+1

def square(x):
    return x**2
def cascade_processing(data, *steps):
    x=[]
    for xx in steps:
        x=list(map(xx,data))
    print(x)   

cascade_processing([1,2,3,6,8,9],add_one,square)

'''Условное применение функции"
Описание:
Напишите функцию conditional_apply(data, condition, transform), которая принимает:

data — список чисел.
condition — функция, возвращающая True или False для числа.
transform — функция, преобразующая число.
Функция должна:

Применять функцию transform только к тем элементам списка, которые удовлетворяют условию condition.
Вернуть новый список.
Пример:

def is_even(x):
    return x % 2 == 0

def double(x):
    return x * 2

print(conditional_apply([1, 2, 3, 4], is_even, double)) '''

def conditional_apply(data, condition, transform):
    app=[]
    for dataa in data:
        if condition(dataa):
            app.append(transform(dataa))
        else: app.append(dataa)
    print(app)    

def is_even(x):
    return x % 2 == 0

def double(x):
    return x * 2

conditional_apply([1, 2, 3, 4], is_even, double)

'''Задача 5: "Генерация функций на лету"
Описание:
Напишите функцию generate_multiplier(n), которая возвращает новую функцию, умножающую входное число на n.

Пример:

multiplier_2 = generate_multiplier(2)
multiplier_5 = generate_multiplier(5)

print(multiplier_2(10))  # 20
print(multiplier_5(10))  # 50'''

def  generate_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier


multiplier_2 = generate_multiplier(2)
multiplier_5 = generate_multiplier(5)

print(multiplier_2(10))  # 20
print(multiplier_5(10))  # 50


'''Задача 6: "Сравнение функций"
Описание:
Напишите функцию compare_functions(data, *functions), которая:

Применяет каждую функцию из *functions ко всем элементам списка data.
Сравнивает результаты каждой функции и возвращает список из лучших значений (например, максимальных).
Пример:

def square(x):
    return x ** 2

def halve(x):
    return x / 2

print(compare_functions([1, 2, 3, 4], square, halve))  
# [1, 4, 9, 16] (результаты square, так как они больше, чем halve)'''

def compare_functions(data, *functions):
    xx=[]
    for x in functions:
        xx.append(list(map(x,data)))  
    print(max(xx))
def square(x):
    return x ** 2

def halve(x):
    return x / 2

compare_functions([1, 2, 3, 4], square, halve)

'''Напишите функцию call_tracker(data, *functions), которая:

Применяет функции к списку.
Возвращает словарь, где:
Ключ — имя функции.
Значение — количество элементов, к которым функция была успешно применена.
Пример:

def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0

print(call_tracker([6, -2, 15, -9, 8, 0], is_even, is_positive))  
# {'is_even': 4, 'is_positive': 3}'''
def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0
def call_tracker(data, *functions):
    all={}
    for func in functions:
        all[func.__name__]=len(list(filter(func,data)))
    print(all)
    

call_tracker([6, -2, 15, -9, 8, 0], is_even, is_positive)    

'''Задача 8: "Группировка по результату"
Описание:
Напишите функцию group_by_result(data, *functions), которая:

Применяет все функции к элементам списка.
Группирует элементы по результатам выполнения функций.
Пример:

def mod_2(x):
    return x % 2

def mod_3(x):
    return x % 3

print(group_by_result([1, 2, 3, 4, 5, 6], mod_2, mod_3))  
# {'mod_2': {0: [2, 4, 6], 1: [1, 3, 5]}, 
#  'mod_3': {0: [3, 6], 1: [1, 4], 2: [2, 5]}}'''


def group_by_result(data, *functions):
    x={}
    count=0
    for func in functions:
        x[func.__name__]=[]
        x[func.__name__].append((list(filter(func, data))))
        count+=1
    print(x)    
def mod_2(x):
    return x % 2

def mod_3(x):
    return x % 3

group_by_result([1, 2, 3, 4, 5, 6], mod_2, mod_3)
'''Задача 1: "Динамическая трансформация"
Описание: Напишите функцию dynamic_transform(data, conditions, transforms), которая принимает:

data — список чисел.
conditions — список функций, каждая из которых возвращает True или False для элемента.
transforms — список функций, каждая из которых преобразует элемент.
Функция должна:

Для каждого элемента применить все условия из conditions.
Если хотя бы одно условие выполнено, применить соответствующую функцию из transforms (по индексу).
Вернуть новый список, где каждый элемент преобразован, если условия выполнены.
Пример:

def is_even(x):
    return x % 2 == 0

def is_negative(x):
    return x < 0

def double(x):
    return x * 2

def negate(x):
    return -x

print(dynamic_transform([1, -2, 3, -4], [is_even, is_negative], [double, negate]))
# [-2, -2, 3, -8]'''  

def dynamic_transform(data, conditions, transforms):
    xx=[]
    for x in data:
        if conditions[0](x) or conditions[1](x):
            xx.append(transforms[1](transforms[0](x)))
    print(xx)     
    result = []
    for item in data:
        transformed = item
        for index, condition in enumerate(conditions):
            if condition(item):  # Если условие выполнено
                transformed = transforms[index](transformed)
                break  # Применяем только одно преобразование
        result.append(transformed)
    print(result) 



         


def is_even(x):
    return x % 2 == 0

def is_negative(x):
    return x > 0

def double(x):
    return x * 2

def negate(x):
    return -x    

dynamic_transform([1, -2, 3, -4], [is_even, is_negative], [double, negate])








