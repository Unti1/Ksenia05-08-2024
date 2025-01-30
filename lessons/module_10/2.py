from threading import Thread
from queue import Queue
import time

class User:
    def __init__(self, name:str, point:int):
        self.name = name
        self.point = point
    def __str__(self):
        return f"{self.name}: {self.point}"

# point - 1 вопрос
# point - 2 оформление продукта


class ConsultCassa(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            user: User = self.queue.get()
            print(f'Текущая очередь: {self.queue}')
            if user.point == 1:
                print(f"Консультант из первой кассы обслуживает {user.name} с целью {user.point}")
                time.sleep(2)
                print(f"Консультант из первой кассы закончил обслуживание")
            else:
                print(f"Пользователь {user} пришел не в ту кассу(касса 1)")
                self.queue.put(user)

class OforderingCassa(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            user: User = self.queue.get()
            print(f'Текущая очередь: {self.queue}')
            if user.point == 2:
                print(f"Консультант из второй кассы обслуживает {user.name} с целью {user.point}")
                time.sleep(4)
                print(f"Консультант из второй кассы закончил оформление продукта")
            else:
                print(f"Пользователь {user} пришел не в ту кассу(касса 2)")
                self.queue.put(user)


if __name__ == "__main__":
    queue = Queue()
    queue.put(User("Иван", 1))
    queue.put(User("Мария", 2))
    queue.put(User("Игорь", 2))
    queue.put(User("Михаил", 1))
    queue.put(User("Алексей", 1))

    c1 = OforderingCassa(queue)
    c2 = ConsultCassa(queue)

    c1.start()
    c2.start()

    c1.join()
    c2.join()
