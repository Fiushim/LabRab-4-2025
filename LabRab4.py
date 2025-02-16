from typing import Optional


class Aircraft:
    """
    Базовый класс для всех самолетов.
    """

    def __init__(self, model: str, manufacturer: str, year: int, max_speed: float):
        """
        Конструктор класса Aircraft.

        :param model: Модель самолета (строка).
        :param manufacturer: Производитель самолета (строка).
        :param year: Год выпуска самолета (целое число).
        :param max_speed: Максимальная скорость самолета в км/ч (число с плавающей точкой).
        """
        self._model = model  # Защищенный атрибут, чтобы предотвратить случайное изменение извне.
        self._manufacturer = manufacturer  # Защищенный атрибут, чтобы предотвратить случайное изменение извне.
        self.year = year  # Публичный атрибут, так как год выпуска может быть легко изменен.
        self.max_speed = max_speed  # Публичный атрибут, так как максимальная скорость может меняться при модификации.

    def __str__(self) -> str:

        return f"{self._manufacturer} {self._model} ({self.year})"

    def __repr__(self) -> str:

        return f"Aircraft(model={self._model}, manufacturer={self._manufacturer}, year={self.year}, max_speed={self.max_speed})"

    def take_off(self) -> None:
        """
        Метод для имитации взлета самолета.
        """
        print(f"{self._manufacturer} {self._model} выполняет взлет.")


class PassengerAircraft(Aircraft):
    """
    Дочерний класс для пассажирских самолетов.
    """

    def __init__(self, model: str, manufacturer: str, year: int, max_speed: float, seating_capacity: int):

        super().__init__(model, manufacturer, year, max_speed)
        self.seating_capacity = seating_capacity  # Публичный атрибут, так как количество мест может меняться.

    def __str__(self) -> str:

        return f"{super().__str__()} - Вместимость: {self.seating_capacity} человек"

    def take_off(self) -> None:

        if self.seating_capacity > 0:
            super().take_off()
        else:
            print("Ошибка: Недостаточно пассажиров для выполнения рейса.")

    def calculate_fuel_consumption(self, distance: float) -> float:
        """
        Вычисляет расход топлива на заданное расстояние.
        """
        average_consumption = 5  # Средний расход топлива на 100 км для пассажирских самолетов (пример).
        return distance * (average_consumption / 100)


class CargoAircraft(Aircraft):
    """
    Дочерний класс для грузовых самолетов.
    """

    def __init__(self, model: str, manufacturer: str, year: int, max_speed: float, load_capacity: float):

        super().__init__(model, manufacturer, year, max_speed)
        self.load_capacity = load_capacity  # Публичный атрибут, так как грузоподъемность может меняться.

    def __str__(self) -> str:


        return f"{super().__str__()} - Грузоподъемность: {self.load_capacity} тонн"

    def take_off(self) -> None:

        if self.load_capacity > 0:
            super().take_off()
        else:
            print("Ошибка: Самолет не загружен. Взлет невозможен.")

    def calculate_payload(self, weight: float) -> bool:

        return weight <= self.load_capacity


if __name__ == "__main__":
    # Пример использования классов
    passenger_plane = PassengerAircraft(
        model="Superjet 100",
        manufacturer="Sukhoi",
        year=2022,
        max_speed=830,
        seating_capacity=98
    )

    cargo_plane = CargoAircraft(
        model="747-400F",
        manufacturer="Boeing",
        year=2018,
        max_speed=905,
        load_capacity=112  # Грузоподъемность Boeing 747-400F составляет до 112 тонн
    )

    print(passenger_plane)  # Выводит информацию о пассажирском самолете
    print(cargo_plane)  # Выводит информацию о грузовом самолете

    passenger_plane.take_off()  # Взлет пассажирского самолета
    cargo_plane.take_off()  # Взлет грузового самолета

    print(passenger_plane.calculate_fuel_consumption(2000))  # Расчет расхода топлива для пассажирского самолета
    print(cargo_plane.calculate_payload(100))  # Проверка возможности загрузки грузового самолета