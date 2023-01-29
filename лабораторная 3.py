class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    @property  # декоратор для геттера
    def pages(self):
        return self._pages

    @pages.setter  # декоратор для сеттера
    def pages(self, value):
        if isinstance(value, int):  # делаем проверку на то, что число страниц целое
            if value > 0:  # проверяем, что число страниц больше нуля (хотя бы одна страница)
                self.pages = value  # устанавливаем значение через setter
            else:
                raise ValueError(f'Invalid number of pages: {value!r}')
        else:
            raise ValueError(f'Number of pages must be int, while input:{value!r} ')

    def __str__(self):  # здесь перегрузка нужна для вывода дополнительного параметра
        tmp_str = super.__str__(self)  # наследование параметров базового класса
        return f"{tmp_str}. Количество страниц {self.pages}"  # дополнение атрибутом бумажной книги

    def __repr__(self):  # для бумажных книг есть необходимый параметр (число страниц), поэтому нужна перегрузка
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float):
            if value > 0:
                self._duration = value
            else:
                raise ValueError(f'Invalid duration: {value!r}')
        else:
            raise ValueError(f'duration must be float, while input:{value!r} ')

    def __str__(self):
        tmp_str = super.__str__(self)
        return f"{tmp_str}. Длительность {self.duration}"  # у базового класса нет длительности

    def __repr__(self):  # для аудиокниг есть необходимый параметр (длительность), поэтому нужна перегрузка
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
