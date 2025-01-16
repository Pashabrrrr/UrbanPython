def add_everything_up(a, b):
    try:
        # Пытаемся выполнить сложение
        return a + b
    except TypeError:
        # Обработка исключения, если типы разные
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(123.456, 7.004))
print(add_everything_up('строка_1', 'строка_2'))