# Импорт необходимых библиотек
import requests
import pandas as pd
import numpy as np


# --------------------------
# 1. Работа с библиотекой requests
# --------------------------
def demo_requests():
    """Демонстрация работы с requests"""
    try:
        # Указываем заголовки для имитации браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Выполняем GET-запрос
        response = requests.get('https://www.e1.ru', headers=headers, timeout=10)

        # Проверяем статус ответа
        print(f"1. Статус код: {response.status_code}")

        # Выводим заголовки ответа
        print("\n2. Заголовки ответа:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        # Выводим первые 300 символов контента
        print("\n3. Часть содержимого страницы:")
        print(response.text[:300])

    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")


# --------------------------
# 2. Работа с библиотекой pandas
# --------------------------
def demo_pandas():
    """Демонстрация работы с pandas"""
    try:
        # Создаем тестовый файл с данными
        data = '''Name,Age,City
                Alice,28,New York
                Bob,32,London
                Charlie,45,Paris
                Dina,23,Berlin'''

        with open('file.txt', 'w') as f:
            f.write(data)

        # Чтение данных из файла
        df = pd.read_csv('file.txt', sep=',')

        # 1. Вывод первых 3 строк
        print("\nПервые 3 записи:")
        print(df.head(3))

        # 2. Основная статистика
        print("\nСтатистика по возрасту:")
        print(df['Age'].describe())

        # 3. Группировка по городам
        print("\nСредний возраст по городам:")
        print(df.groupby('City')['Age'].mean())

    except Exception as e:
        print(f"Ошибка в работе с pandas: {e}")


# --------------------------
# 3. Работа с библиотекой numpy
# --------------------------
def demo_numpy():
    """Демонстрация работы с numpy"""
    try:
        # Создание массива
        arr = np.arange(1, 14)
        print("\nИсходный массив:")
        print(arr)

        # 1. Математические операции
        print("\nУмножение на 2:")
        print(arr * 2)

        # 2. Изменение формы массива
        reshaped = arr.reshape(13, 1)
        print("\nМассив после изменения формы:")
        print(reshaped)

        # 3. Статистические показатели
        print(f"\nСумма элементов: {arr.sum()}")
        print(f"Среднее значение: {arr.mean():.2f}")
        print(f"Стандартное отклонение: {arr.std():.2f}")

    except Exception as e:
        print(f"Ошибка в работе с numpy: {e}")


# --------------------------
# Главная функция
# --------------------------
if __name__ == "__main__":
    print("=" * 40 + "\nДемонстрация работы с requests:\n" + "=" * 40)
    demo_requests()

    print("\n" + "=" * 40 + "\nДемонстрация работы с pandas:\n" + "=" * 40)
    demo_pandas()

    print("\n" + "=" * 40 + "\nДемонстрация работы с numpy:\n" + "=" * 40)
    demo_numpy()