'''Цель: Применить очереди в работе с потоками, используя класс Queue.

Задача "Потоки гостей в кафе":
Необходимо имитировать ситуацию с посещением гостями кафе.
Создайте 3 класса: Table, Guest и Cafe.
Класс Table:
Объекты этого класса должны создаваться следующим способом - Table(1)
Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
Класс Guest:
Должен наследоваться от класса Thread (быть потоком).
Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
Обладать атрибутом name - имя гостя.
Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
Класс Cafe:
Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
Метод guest_arrival(self, *guests):
Должен принимать неограниченное кол-во гостей (объектов класса Guest).
Далее, если есть свободный стол, то сажать гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку
"<имя гостя> сел(-а) за стол номер <номер стола>".
Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
Метод discuss_guests(self):
Этот метод имитирует процесс обслуживания гостей.
Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки 
"<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый 
из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
Далее запустить поток этого гостя (start)
Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
Table - стол, хранит информацию о находящемся за ним гостем (Guest).
Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).

Пример результата выполнения программы:
Выполняемый код:
class Table:
...
class Guest:
...
class Cafe:
...
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):
Maria сел(-а) за стол номер 1
Oleg сел(-а) за стол номер 2
Vakhtang сел(-а) за стол номер 3
Sergey сел(-а) за стол номер 4
Darya сел(-а) за стол номер 5
Arman в очереди
Vitoria в очереди
Nikita в очереди
Galina в очереди
Pavel в очереди
Ilya в очереди
Alexandra в очереди
Oleg покушал(-а) и ушёл(ушла)
Стол номер 2 свободен
Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
.....
Alexandra покушал(-а) и ушёл(ушла)
Стол номер 4 свободен
Pavel покушал(-а) и ушёл(ушла)
Стол номер 3 свободен
Примечания:
Для проверки значения на None используйте оператор is (table.guest is None).
Для добавления в очередь используйте метод put, для взятия - get.
Для проверки пустоты очереди используйте метод empty.
Для проверки выполнения потока в текущий момент используйте метод is_alive.
Файл module_10_4.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!'''
import threading
import random
import time
from queue import Queue
class Table:
    def __init__(self,number):
        self.number=number
        self.guest=None
class Guest(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        x=random.uniform(1,10)
        time.sleep(x)
        print(f"{self.name} покушал(-а) и ушёл(ушла)")
class Cafe:
    def __init__(self,queue,*tables:Table):
        self.tables=tables
        self.queue=Queue()
    def guest_arrival(self, *guests:Guest): 
        for guest in guests:
            x=False
            for table in self.tables:
                if table.guest is None:
                    table.guest=guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()  # Запуск потока гостя
                    x = True
                    break
            if not x:
                    print(f'"{guest.name} в очереди"')
                    self.queue.put(guest)
    def discuss_guests(self) :
        for table in self.tables:
            if table.guest and not table.guest.is_alive():
                print(f'{table.guest.name} покушал(-а) и ушёл(ушла)"')
                print(f'"Стол номер {table.number} свободен"')
                table.guest = None
                
            if not self.queue.empty() and not table.guest:
                guest = self.queue.get()  # Берём первого гостя из очереди
                table.guest = guest
                print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                guest.start() 



            






if __name__ == "__main__":
    queue = Queue()
    tables = [Table(number) for number in range(0, 5)]
# Имена гостей
    guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
    guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
    cafe = Cafe(*tables)
# Приём гостей
    cafe.guest_arrival(*guests)
while any(table.guest for table in tables):  # Пока хотя бы один стол занят
    cafe.discuss_guests()
    time.sleep(1)    
for guest in guests:
        guest.join()     



            
  
                




        



