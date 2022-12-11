class Car:
    def __init__(self, color: str, count_door, serial_numb: str):
        if not isinstance(color, str):
            raise TypeError('Название цвета должно быть типа str')
        self.color = color
        if count_door <= 0:
            raise TypeError('Машины без дверей не бывает!')
        self.count_door = count_door
        if not isinstance(serial_numb, str):
            raise TypeError('Номер должен совершать буквы и цифры')
        self.serial_numb = serial_numb

    def broken(self):
        print('Машина не двигается')
        self.health = 0


class Airplaine:
    def __init__(self, flight_comp: str, capacity: int, turbines):
        if not isinstance(flight_comp, str):
            raise TypeError('Название авиа компании должено быть типа str')
        self.flight_comp = flight_comp
        if not capacity > 20:
            raise ValueError('Ожидается самолет больше чем с 20 пассажирами на борту')
        self.capacity = capacity
        if turbines > 4:
            raise ValueError('У самолета не больше четырех турбин')
        self.turbines = turbines


class Houses:
    def __init__(self, number_of_floors: int, entrance: int):
        if not isinstance(number_of_floors, int):
            raise TypeError('Лучше записать количество этажей цифровым значением')
        if number_of_floors <= 0:
            raise ValueError('Не может быть дом без этажей')
        self.height = number_of_floors
        if entrance <= 0:
            raise ValueError('У дома должен быть вход!!!')
        self.entrance = entrance


if __name__ == "__main__":
    Hyundai_Tucson_1 = Car('Синий', 5, 'KZ587234')
    Hyundai_Tucson_2 = Car('Красный', 5, 'KZ9834718')
    boeing747 = Airplaine('Аэрофлот', 111, 4)
    house_1 = Houses(9, 2)
    house_2 = Houses(1, 1)
    import doctest

    doctest.testmod()
    pass