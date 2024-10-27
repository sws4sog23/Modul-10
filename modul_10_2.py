import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.n = 0
    def battle(self, name, power, counter=100):
        # print(f'{self.name}, на нас напали!')
        power = int(self.power)

        while counter > 0:
            time.sleep(1)
            self.n += 1
            counter -= power
            print(f'{self.name} сражается {self.n} день(дня)..., осталось {counter} воинов.',)

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle(self.name, self.power)
        print(f'{self.name} одержал победу спустя {self.n} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
