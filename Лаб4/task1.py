from datetime import datetime

if __name__ == "__main__":
    class Vehicle:
        """
        Базовый класс - автомобили

        Атрибуты:
            brand(str): Марка транспортного средства
            model(str): Модель транспортного средства
            year (int): Год выпуска
            license_plate (str): Номер
            _mileage (float): Пробег

        """

        def __init__(self, brand: str, model: str, year: int, license_plate: str, mileage: float = 0.0):
            """
            Конструктор базового класса Vehicle
            """
            self.brand = brand
            self.model = model
            self.year = year
            self._mileage = mileage
            self.license_plate = license_plate

        def __str__(self) -> str:
            """
            Магический метод __str__ базового класса Vechicle
            Возвращает строковое представление объекта
            """
            return f"{self.__class__.__name__}{self.brand} {self.model} {self.license_plate} {self.year} year"

        def __repr__(self) -> str:
            """
            Магический метод __repr__ базового класса Vechicle
            Возвращает формальное строковое представление объекта

            """
            return f"Vehicle(brand={self.brand}, model={self.model}, year={self.year}, license_plate={self.license_plate}, mileage={self._mileage})"

        @property
        def mileage(self) -> float:
            """
            Getter для получения текущего пробега транспортного средства

            :return: Пробег транспортного средства
            """
            return self._mileage

        @mileage.setter
        def mileage(self, distance: float) -> None:
            """
            Setter для увеличения пробега транспортного средства

            :param distance: Расстояние, на которое проехало транспортное средство
            """
            if distance < 0:
                raise ValueError("Пробег не может быть отрицательным.")
            self._mileage += distance

        def get_age(self) -> int:
            """
            Возвращает возраст транспортного средства в годах

            :return: Возраст транспортного средства
            """
            current_year = datetime.now().year
            return current_year - self.year

        def maintenance_cost(self, base_cost: float, cost_per_km: float) -> float:
            """
            Метод базового класса Vehicle для расчета стоимости обслуживания транспортного средства

            :param base_cost: Базовая стоимость обслуживания
            :param cost_per_km: Дополнительная стоимость за каждый км пробега

           :return: Cтоимость обслуживания
            """

            return base_cost + (self._mileage * cost_per_km)

    class Car(Vehicle):
        """
        Дочерний класс - легковые автомобили

        Атрибуты:
            brand (str): Марка автомобиля
            model (str): Модель автомобиля
            year (int): Год выпуска
            license_plate (str): Номер
            _mileage (float): Пробег
            num_doors (int): Количество дверей
        """

        def __init__(self, brand: str, model: str, year: int, license_plate: str,  mileage: float = 0.0, num_doors: int = 4):
            """
            Конструктор дочернего класса Car

            """
            super().__init__(brand, model, year, license_plate, mileage)
            self.num_doors = num_doors

        def __repr__(self) -> str:
            """
            Перегрузка магического метода __repr__ для дочернего класса Car
            Возвращает формальное строковое представление объекта

            """
            return f"Car(brand={self.brand}, model={self.model}, year={self.year}, license_plate={self.license_plate}, mileage={self._mileage}, num_doors={self.num_doors})"

        def honk(self) -> str:
            """
            Метод дочернего класса Car, который возвращает звук сигнала автомобиля

            :return: Строка с описанием звука сигнала
            """
            return "Beep Beep!"

        def maintenance_cost(self, base_cost: float, cost_per_km: float) -> float:
            """
            Перегрузка метода для расчета стоимости обслуживания для легкового автомобиля
            Учитывается также возраст машины


           :return: стоимость обслуживания
            """
            base_cost = super().maintenance_cost(base_cost, cost_per_km)  # Получаем базовую стоимость из метода базового класса
            age_multiplier = 1 + self.get_age() * 0.02  # Множитель в зависимости от возраста автомобиля
            return base_cost * age_multiplier

    class Truck(Vehicle):
        """
        Дочерний класс - грузовые автомобили

        Атрибуты:
            brand (str): Марка грузовика
            model (str): Модель грузовика
            year (int): Год выпуска
            license_plate (str): Номер
            mileage (float): Пробег
            max_load (float): Максимальная грузоподъемность (в тоннах)
        """

        def __init__(self, brand: str, model: str, year: int, license_plate: str, mileage: float = 0.0, max_load: float = 10.0):
            """
            Конструктор дочернего класса Truck

            :param brand: Марка
            :param model: Модель
            :param year: Год выпуска
            :param mileage: Пробег (по умолчанию 0.0)
            :param max_load: Максимальная грузоподъемность (по умолчанию 10.0 тонн)
            """
            super().__init__(brand, model, year, license_plate, mileage)
            self.max_load = max_load

        def __repr__(self) -> str:
            """
            Перегрузка магического метода __repr__ для дочернего класса Truck
            Возвращает формальное строковое представление объекта

            """
            return f"Truck(brand={self.brand}, model={self.model}, year={self.year}, license_plate={self.license_plate}, mileage={self._mileage}, max_load={self.max_load})"

        def load_cargo(self, weight: float) -> str:
            """
            Метод для загрузки груза в грузовик

            :param weight: Вес груза (в тоннах)

            :return: Сообщение о результате загрузки
            """
            if weight > self.max_load:
                return "Груз слишком тяжелый для этого грузовика"
            else:
                return f"Груз весом {weight} тонн успешно загружен"

   #Строки ниже нужны для проверки работоспособности классов

    car = Car(brand="Toyota", model="Camry", year=2020, license_plate="A123BC", mileage=15000, num_doors=4)
    truck = Truck(brand="Volvo", model="FMX", year=2022, license_plate="X456YZ", mileage=30000, max_load=10)

    print(car)
    print(repr(car))
    print(truck)
    print(repr(truck))

    print(car.get_age())

    print(car.maintenance_cost(200, 0.05))
    print(truck.maintenance_cost(200, 0.05))

    print(truck.load_cargo(8))
    print(truck.load_cargo(12))

    car.mileage = 100
    print(f"Новый пробег легкового автомобиля: {car.mileage} км")

    pass
