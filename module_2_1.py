# module_2_1

first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: "))
if first == second and first == third:
    print("Все 3 числа одинаковые")
elif first == second or second == third or first == third:
    print("Только 2 числа одинаковые")
else:
    print("Одинаковых чисел нет")
