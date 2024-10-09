# Глобальная область
s = 10
d = 29
def func():
    # Локальная область
    s = 20
    def func2():
        nonlocal s
        s = 30
        print("Локальное пространство для функции func2() :", locals())
    print("Локальное пространство для функции func() :", locals())
    func2()
    print("Локальное пространство для функции func() ПОСЛЕ работы func2() :", locals())


print(f'Глобальная область: {s=}',)
func()
print(f'Глобальная область: {s=}')
# print(globals())
print(__file__)