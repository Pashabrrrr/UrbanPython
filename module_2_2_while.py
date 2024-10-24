my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i <= len(my_list):
    n = my_list[i]
    if n > 0:
        print(n)
        i = i + 1
    elif n == 0:
        i = i + 1
        continue
    elif n < 0:
        break

print("Встретили отрицательное или список чисел закончился")
