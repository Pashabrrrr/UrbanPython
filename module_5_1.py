
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name},  Кол-во эатжей: {self.number_of_floors}')

house1 = House('ЖК Крылья', 16)
house2 = House('ЖК Светлый', 18)

print(house1)
print(house2)

print(len(house1))
print(len(house2))