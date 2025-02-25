def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result <= 1:
            print('Составное')  # Числа меньше или равные 1 не являются простыми
            return result
            # Проверяем, является ли число простым
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print('Составное')
                return result
        print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)  # Ожидаем: "Простое\n11"