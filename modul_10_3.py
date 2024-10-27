import threading
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        count = 100

        while count > 0:
            random_n = randint(50, 500)
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            self.balance += random_n
            count -= 1
            print(f'Пополнение: {random_n}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        count = 100

        while count > 0:
            if self.lock.locked() == True:
                self.lock.release()
            random_n = randint(50, 500)
            print(f'Запрос на {random_n}')
            if random_n <= self.balance:
                self.balance -= random_n
                print(f'Снятие: {random_n}. Баланс: {self.balance}')
                count -= 1
                time.sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
