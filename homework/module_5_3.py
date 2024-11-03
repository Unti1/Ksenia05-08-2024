'''Домашняя работа по уроку "Перегрузка операторов"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.

Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

Необходимо дополнить класс House следующими специальными методами:
eq(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы lt(<), le(<=), gt(>), ge(>=), ne(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе eq в сравнении участвует кол-во этажей.
add(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
radd(self, value), iadd(self, value) - работают так же как и add (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов eq, add  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.

Пример результата выполнения программы:
Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # eq

h1 = h1 + 10 # add
print(h1)
print(h1 == h2)

h1 += 10 # iadd
print(h1)

h2 = 10 + h2 # radd
print(h2)

print(h1 > h2) # gt
print(h1 >= h2) # ge
print(h1 < h2) # lt
print(h1 <= h2) # le
print(h1 != h2) # ne

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False

Примечания:
Методы iadd и radd не обязательно описывать заново, достаточно вернуть значение вызова add.
Более подробно о работе всех перечисленных методов можно прочитать здесь и здесь.

Файл module_5_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него'''
class House:
    def __init__(self,name:str,kolvo:int):
        self.name = name 
        self.number_of_floors = kolvo # 2

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
        return NotImplemented

    def __lt__(self,other):
        if isinstance(other, House):
            return other.number_of_floors > self.number_of_floors
        return NotImplemented
    
    def __le__(self,other):
        if isinstance(other, House):
            return other.number_of_floors <= self.number_of_floors
        return NotImplemented
    
    def __gt__(self,other):
        if isinstance(other, House):
            return other.number_of_floors > self.number_of_floors
        return NotImplemented
    
    def __ge__(self,other):
        if isinstance(other, House):
            return other.number_of_floors >= self.number_of_floors
        return NotImplemented
    
    def __ne__(self,other):
        if isinstance(other, House):
            return other.number_of_floors != other.number_of_floors
        return NotImplemented
    
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented
     
    def __radd__(self, value):
        return self.__add__(value)

    
    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # eq

h1 = h1 + 10 # add
print(h1)
print(h1 == h2)

h1 += 10 # iadd
print(h1)

h2 = 10 + h2 # radd
print(h2)

print(h1 > h2) # gt
print(h1 >= h2) # ge
print(h1 < h2) # lt
print(h1 <= h2) # le
print(h1 != h2) # ne



        
        