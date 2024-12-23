class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Список допустимых цветов

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner  # Владелец
        self.__model = model  # Модель (сокрытый атрибут)
        self.__engine_power = engine_power  # Мощность двигателя (сокрытый атрибут)
        self.__color = color  # Цвет (сокрытый атрибут)

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in (color.lower() for color in Vehicle.__COLOR_VARIANTS):
            self.__color = new_color  # Меняем цвет если он допустимый
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Максимальное число пассажиров в седане

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)  # Инициализация родительского класса


# Создание объекта класса Sedan
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')  # Неправильный цвет
vehicle1.set_color('BLACK')  # Правильный цвет
vehicle1.owner = 'Vasyok'  # Изменение владельца

# Проверяем что поменялось
vehicle1.print_info()