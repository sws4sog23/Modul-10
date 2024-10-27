import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self, name, power, counter=100):
        # print(f'{self.name}, на нас напали!')
        power = int(self.power)
        n = 0

        while counter > 0:
            time.sleep(1)
            n += 1
            counter -= power
            print(f'{self.name} сражается {n} день(дня)..., осталось {counter} воинов.',)
        if counter <= 0:
            print(f'{self.name} одержал победу спустя {n} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle(self.name, self.power)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
