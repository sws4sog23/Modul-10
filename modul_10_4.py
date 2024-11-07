from queue import Queue
import threading
import time
from random import randint

queue_c = Queue()
t_g = {}

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

        t_g[self.number] = self.guest
class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        random_n = randint(3, 10)
        time.sleep(random_n)
class Cafe:
    def __init__(self, *tabls):
        self.tabls = tabls
        self.queue_c = queue_c

    def guest_arrival(self, *guests):
        for name in guests:
            for k, v in t_g.items():
                if v == None:
                    t_g[k] = name
                    print(f'{name.name} сел(-а) за стол номер {k}')
                    name.start()
                    break
                elif not None in t_g.values():
                    queue_c.put(name)
                    print(f'{name.name} в очереди')
                    break

    def discuss_guests(self):
        while not queue_c.empty() or not flg:
            flg = True
            for k, v in t_g.items():
                if v != None:
                    flg = False
                    if v.is_alive() == False:
                        print(f'{v.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {k} свободен')
                        t_g[k] = None
                        if queue_c.empty() == False:
                            t_g[k] = queue_c.get()
                            print(f'{t_g[k].name} вышел(-ла) из очереди и сел(-а) за стол номер {k}')
                            t_g[k].start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# print('гости',guests) #t
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()







