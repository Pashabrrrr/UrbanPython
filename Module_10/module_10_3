import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Создаем объект Lock для блокировки

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерируем случайное число для пополнения
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                # Если баланс >= 500 и замок заблокирован, разблокируем его
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            time.sleep(0.001)  # Имитация задержки

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерируем случайное число для снятия
            print(f"Запрос на {amount}")
            with self.lock:  # Блокируем доступ к балансу
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    # Блокируем поток
                    self.lock.acquire()
            time.sleep(0.001)  # Имитация задержки

# Создаем объект класса Bank
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ждем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
