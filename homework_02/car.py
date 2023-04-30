"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int, *args, **kwargs):
        super().__init__(weight, fuel, fuel_consumption)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.engine = Engine(volume=3.5, pistons=6)

    def set_engine(self, engine: Engine):
        if isinstance(engine, Engine):
            self.engine = engine
