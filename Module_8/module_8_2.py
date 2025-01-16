def personal_sum(numbers):
    result = 0  # Переменная для хранения суммы
    incorrect_data = 0  # Счетчик некорректных данных

    for item in numbers:
        try:
            result += item  # Пытаемся добавить элемент к результату
        except TypeError:
            # Если элемент некорректного типа, увеличиваем счетчик и сообщаем о некорректном типе
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Пытаемся рассчитать сумму и количество
        total_sum, incorrect_data_count = personal_sum(numbers)
        total_count = len(numbers) - incorrect_data_count

        if total_count == 0:
            return 0  # Если нет корректных чисел, возвращаем 0

        return total_sum / total_count  # Возвращаем среднее арифметическое
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None  # В случае некорректного типа возвращаем None


# Примеры использования функции
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Вывод: 0
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Вывод: 2.0
print(f'Результат 3: {calculate_average(567)}')  # Вывод: None
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Вывод: 26.5