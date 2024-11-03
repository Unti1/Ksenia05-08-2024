'''2023/10/30 00:00|Домашняя работа по уроку "Специальные методы классов"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: понять как работают базовые магические методы на практике.

Задача "Магические здания":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

Необходимо дополнить класс House следующими специальными методами:
len(self) - должен возвращать кол-во этажей здания self.number_of_floors.
str(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

Пример результата выполнения программы:
Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# str
print(h1)
print(h2)

# len
print(len(h1))
print(len(h2))

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20

Примечания:

Файл module_5_2.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.'''

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
    


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)   
h2.go_to(10)    
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# str
print(h1)
print(h2)

# len
print(len(h1))
print(len(h2))

