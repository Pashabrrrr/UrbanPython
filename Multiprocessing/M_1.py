import multiprocessing
from datetime import datetime


def read_info(name):
    """Читает файл построчно и сохраняет строки в локальный список"""
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Выход при пустой строке (конец файла)
                break
            all_data.append(line)
    # Список all_data не возвращаем для экономии памяти


if __name__ == '__main__':
    # 1. Подготовка списка файлов (пример для 4 файлов)
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # 2. Линейное выполнение (раскомментировать для теста)
    start = datetime.now()
    for file in filenames:
        read_info(file)
    print(f"Линейное время: {datetime.now() - start}")

    # 3. Многопроцессное выполнение (раскомментировать для теста)
    start = datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    print(f"Многопроцессное время: {datetime.now() - start}")