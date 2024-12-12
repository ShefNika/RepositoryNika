class Table:

    def __init__(self, material: str, color: str):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола
        :param color: Цвет стола

        Примеры:
        >>> table = Table("wood", "brown") # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = material
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color

    def legs(self, leg: int) -> str:
        """
        Функция с дополнительным описанием количества ножек стола

        :param leg: Количество ножек

        :return: Строка с полным описанием стола

        Примеры:
        >>> table = Table("wood", "brown")
        >>> table.legs(4)
        """
        ...

    def is_available(self) -> bool:
        """
        Функция возвращающая, доступен ли стол к покупке

        :return: true/false

        Примеры:
        >>> table = Table("wood", "brown")
        >>> table.is_available()
        """
        ...


class Tree:

    def __init__(self, species: str, height: float):
        """
       Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева в метрах

        Примеры:
        >>> oak = Tree("Oak", 15.0)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        self.species = species
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

    def grow(self, years: int) -> None:
        """
        Функция увеличения высоты дерева за определенное количество лет

        :param years: Количество лет

        Примеры:
        >>> oak = Tree("Oak", 15.0)
        >>> oak.grow(5)
        """
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Количество лет должно быть положительным числом")
        ...

    def where(self) -> str:
        """
        Функция, возвращающая где растет дерево

        :return: Страна, где растет дерево
        Примеры:
        >>> oak = Tree("Oak", 15.0)
        >>> oak.where()
        """
        ...


class SocialMedia:

    def __init__(self, name: str, active_users: int):
        """
        Инициализация социальной сети.

        :param name: Название социальной сети
        :param active_users: Количество активных пользователей

        Примеры:
        >>> fb = SocialMedia("Facebook", 3000000000)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        self.name = name
        if not isinstance(active_users, int) or active_users < 0:
            raise ValueError("Количество активных пользователей должно быть неотрицательным целым числом")
        self.active_users = active_users

    def post_content(self, content: str) -> None:
        """
        Функция размещения контента в социальной сети.

        :param content: Контент для публикации

        Примеры:
        >>> fb = SocialMedia("Facebook", 3000000000)
        >>> fb.post_content("Hello, world!")
        """
        ...

    def find_user(self, user: str) -> int:
        """
        Функция поиска пользователя по его нику

        :param user: Ник пользователя
        :return: Уникальный адрес пользователя

        Примеры:
        >>> fb = SocialMedia("Facebook", 300000000)
        >>> fb.find_user("Ivanov")
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
