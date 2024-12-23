# Родительский класс Animal
class Animal:
    def __init__(self, name):
        self.alive = True     # Живое
        self.fed = False      # Накормленное
        self.name = name      # Имя животного


# Родительский класс Plant
class Plant:
    def __init__(self, name):
        self.edible = False    # Съедобность
        self.name = name       # Имя растения


# Класс-наследник Mammal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:  # Если растение съедобное
            print(f"{self.name} съел {food.name}")
            self.fed = True  # Животное стало накормленным
        else:  # Если растение несъедобное
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # Животное погибло


# Класс-наследник Predator
class Predator(Animal):
    def eat(self, food):
        if food.edible:  # Если растение съедобное
            print(f"{self.name} съел {food.name}")
            self.fed = True  # Животное стало накормленным
        else:  # Если растение несъедобное
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # Животное погибло


# Класс-наследник Flower
class Flower(Plant):
    pass  # Цветы по умолчанию несъедобные


# Класс-наследник Fruit
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)  # Вызов конструктора родительского класса
        self.edible = True  # Переопределяем на съедобное


# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Вывод информации
print(a1.name)  # Имя хищника
print(p1.name)  # Имя цветка
print(a1.alive)  # Жив ли хищник
print(a2.fed)    # Накормлено ли млекопитающее

# Взаимодействия
a1.eat(p1)  # Хищник пытается съесть цветок
a2.eat(p2)  # Млекопитающее ест фрукт

# Проверка состояния после взаимодействий
print(a1.alive)  # Жив ли хищник после еды
print(a2.fed)    # Накормлено ли млекопитающее после еды