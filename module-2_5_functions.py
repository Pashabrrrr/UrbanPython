n = int(input("Введите число строк матрицы: "))
m = int(input("Введите число столбцов матрицы: "))
value = int(input("Введите значение: "))


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        for j in range(m):
            if value > 0:
                list_.append(value)
        matrix.append(list_)

    return matrix


result = get_matrix(n, m, value)
print(*result, sep='\n')
