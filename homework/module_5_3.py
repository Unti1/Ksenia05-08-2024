'''Дополнительно о работе метода new:
Как мы уже знаем метод new вызывается перед тем, как вызовется метод init.
Разберёмся, как происходит передача данных между ними на следующем примере.

Работа new:
'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент. Он будет находиться под индексом 0 как единственный элемент кортежа.
second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы. Они будут находиться под ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.
Передача данных из new в init:
После того как метод new отработает до конца, произойдут следующие события с параметрами init:
В параметр first распакуется из args единственный аргумент 'data'.
В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.


Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод new так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод del(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов del и new, а также значение атрибута houses_history.

Пример результата выполнения программы:
Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

Вывод на консоль:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Эльбрус снесён, но он останется в истории'''

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # print(args, kwargs)
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    
    def __init__(self,name:str,kolvo:int,second = 25,third = 3.14):
        self.name = name 
        self.number_of_floors = kolvo # 2
        self.second = second
        self.third = third
        

    def go_to(self,new_floor):
        
        if new_floor > self.number_of_floors or new_floor< 1:
            print(f'В {self.name} этажа {new_floor} нет. В нем всего {self.number_of_floors} этажей')
        else:
            for i in range(1,new_floor+1):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название:{self.name}, кол-во этажей:{self.number_of_floors}"
    
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    
    def __lt__(self,other):
        if isinstance(other, House):
            return other.number_of_floors > self.number_of_floors
        
    def __le__(self,other):
        if isinstance(other, House):
            return other.number_of_floors <= self.number_of_floors
        
    def __gt__(self,other):
        if isinstance(other, House):
            return other.number_of_floors > self.number_of_floors
        
    def __ge__(self,other):
        if isinstance(other, House):
            return other.number_of_floors >= self.number_of_floors
        
    def __ne__(self,other):
        if isinstance(other, House):
            return other.number_of_floors != other.number_of_floors
        return NotImplemented
    
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        
     
    def __radd__(self, value):
        return self.__add__(value)

    
    def __iadd__(self, value):
        return self.__add__(value)
    
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)



        
        