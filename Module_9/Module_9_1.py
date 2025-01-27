def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем все функции из *functions
    for func in functions:
        # Вызываем функцию и сохраняем результат в словаре
        results[func.__name__] = func(int_list)

        # Возвращаем словарь с результатами
    return results


# Примеры использования функции
print(apply_all_func([6, 20, 15, 9], max, min))  # {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))  # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}