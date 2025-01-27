import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            time.sleep(1)  # Имитация одного дня сражения
            self.days += 1

            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0  # Не может быть отрицательных врагов

            day_word = "день" if self.days == 1 else "дня"
            print(f"{self.name}, сражается {self.days} {day_word}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} {day_word}!")

# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения битв
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")