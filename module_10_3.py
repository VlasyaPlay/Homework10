import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.condition:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500:
                    self.condition.notify_all()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.condition:
                print(f"Запрос на {amount}")
                while amount > self.balance:
                    print("Запрос отклонён, недостаточно средств")
                    self.condition.wait()
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')