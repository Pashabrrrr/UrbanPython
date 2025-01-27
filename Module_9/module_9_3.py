# Даны списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для разницы длин строк, если они не равны
first_result = (abs(len(s1) - len(s2)) for s1, s2 in zip(first, second) if len(s1) != len(s2))

# 2. Генераторная сборка для сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) != len(second[i]) for i in range(len(first)))

# Приводим генераторы к спискам и выводим результаты
print(list(first_result))
print(list(second_result))