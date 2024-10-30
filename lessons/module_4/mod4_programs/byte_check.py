from dis import dis

def some_func():
    a = 'Я из второго модуля'
    print(a)
    return(a)


# print(some_func())
dis(some_func)