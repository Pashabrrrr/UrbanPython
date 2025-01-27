from random import choice

# Задание 1: Лямбда-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
comparison = list(map(lambda x, y: x == y, first, second))
print(comparison)  # Вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Задание 2: Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(f"{data}\n")
    return write_everything

# Пример использования write
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задание 3: Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Пример использования MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())  # Примерный вывод: Да
print(first_ball())  # Примерный вывод: Наверное
print(first_ball())  # Примерный вывод: Нет