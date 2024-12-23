import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = color
        self.filled = False  # Опционально, можете добавить атрибут для заполненности
        self.set_sides(*sides)  # Установка сторон при создании объекта

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
            0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)
        self.__sides = [1]  # У круга только одна сторона
        self.__radius = circumference / (2 * math.pi)  # Вычисляем радиус по длине окружности

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.set_sides(side1, side2, side3)

    def get_square(self):
        s = sum(self.__sides) / 2  # Полупериметр
        return math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length, *args):
        super().__init__(color)
        if args:  # Если переданы другие стороны, игнорируем их
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = [side_length] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3  # Объём куба стороны в кубе


# Пример работы классов

circle1 = Circle((200, 200, 100), 10)  # (Цвет, длина окружности)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 1 (поскольку у круга одна сторона)

# Проверка объёма (куба):
print(cube1.get_volume())  # 216