class Bottle:
    def __init__(self, wrap_status, liquid_status, liquid_capacity):
        """"
        Создание объекта класса "бутылка"
        :param wrap_status: статус бутылки (открыта или закрыта), задаётся латинскими буквами "C" или "O"
        :param liquid_status: текущее количество жидкости в бутылке
        :param liquid_capacity: вместимость бутылки

        Примеры:
        >>> my_bottle = Bottle(0, 10, 100) # инициализация экземпляра класса
        """

        if (wrap_status != 0) and (wrap_status != 1):
            raise ValueError("bottle must be opened (0) or closed (1)")
        self.wrap_status = wrap_status
        if not isinstance(liquid_status, (int, float)):
            raise TypeError("Wrong type for liquid_status")
        if not isinstance(liquid_capacity, (int, float)):
            raise TypeError("Wrong type for liquid_capacity")
        if liquid_status > liquid_capacity:
            raise ValueError("Capacity must be graiter than occupied volume")
        if liquid_status < 0:
            raise ValueError("Amount of liquid must not be lesser than zero")
        if liquid_capacity < 0:
            raise ValueError("Amount of liquid must not be lesser than zero")
        self.liquid_status = liquid_status
        self.liquid_capacity = liquid_capacity

    def open_bottle(self):
        """"
        Функция открывает бутылку, если та была закрыта,
        в случае успеха выводится сообщение (бутылка открыта).
        :raise ValueError: вызывает ошибку, если бутылка была открыта при вызове метода
        Примеры:
        >>> my_bottle = Bottle(1, 10, 100)
        >>> my_bottle.open_bottle()
        """

    ...

    def close_bottle(self):
        """"
        Функция закрывает бутылку, если та была открыта,
        в случае успеха выводится сообщение (бутылка закрыта).
        :raise ValueError: вызывает ошибку, если бутылка была закрыта при вызове метода
        Примеры:
        >>> my_bottle = Bottle(0, 10, 100)
        >>> my_bottle.close_bottle()
        """
        ...

    def add_liquid(self, liquid_input):
        """"
        Функция добавляет жидкость в бутылку, если бутылка открыта
        :raise TypeErroe: вызывает ошибку при попытке налить не целое и не вещественное число жидкости
        :raise ValueError: вызывает ошибку при попытке переполнить бутылку или налить отрицательные значения
        :return: новое число занятого объёма бутылки
        примеры:
        >>> my_bottle = Bottle(0, 10, 100)
        >>> my_bottle.add_liquid(50)
        """
        ...


class Ship:
    def __init__(self, water_displacement, cargo_type):
        """
        Создание объекта класса корабль:
        :param water_displacement: водоизмещение корабля, тонны
        :param cargo_type: тип груза

        Примеры:
        >>> tanker = Ship(100, "Oil")
        """
        if not isinstance(water_displacement, (int, float)):
            raise TypeError("Water displasement must be int or float")
        if water_displacement <= 0:
            raise ValueError("Water displasement must be graiter than 0")
        if not isinstance(cargo_type, str):
            raise TypeError("Name of cargo type must be string")

    def check_displacement(self):
        """
        Метод смотрит водоизмещение корабля
        :return: возвращает значение водоизмещения

        Примеры:
        >>> tanker = Ship(100, "Oil")
        >>> tanker.check_displacement()
        """

    ...

    def check_is_cargo_type(self, type_):
        """
        Метод проверяет соответствие груза корабля с предложенным пользователем типом
        :param type_: груз, с которым сравнивается значение
        :raise ErrorType: вызывает ошибку, если type_ не строковая переменная
        :return: возвращает значение True, если тип груза корабля совпал с type_, False - если не совпал

        Примеры:
        >>> tanker = Ship(100, "Oil")
        >>> tanker.check_is_cargo_type("Water")
        """
        ...


class City:
    def __init__(self, population, area):
        """
        Инициализация объекта город:
        :param population: население города
        :param area: площадь города (в квадратных километрах)
        Примеры:
        >>> pskov = City(209073, 95.5) # PEP8 здесь противоречит тому, что города пишутся с большой буквы
        """
        if not isinstance(population, int):
            raise TypeError("Population must be int!")
        if population <= 0:
            raise ValueError("Population must be graiter than 0")
        if not isinstance(area, (int, float)):
            raise TypeError("Area must be float or int!")
        if area <= 0:
            raise ValueError("Area must be graiter than 0")

    def population_census(self):
        """
        Метод проводит перепись населения
        :return: возвращает новое число населения
        Примеры:
        >>> pskov = City(209073, 95.5)
        >>> pskov.population_census()
        """
        ...

    def city_expand(self, additional_area):
        """
        Метод увеличивает площадь города на additional_area
        :param additional_area: дополнительная площадь города
        :raise TypeError: вызывает ошибку, если тип additional_area не int и не float
        :return: возвращает новую площадь города

        Примеры:
        >>> pskov = City(209073, 95.5)
        >>> pskov.city_expand(10)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()