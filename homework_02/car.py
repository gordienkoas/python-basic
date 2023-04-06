"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine

class Car(Vehicle):
    def __init__(self, weight=int, fuel=int, fuel_consumption=int, *args, **kwargs):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.engine = engine

    def set_engine(self, engine: Engine):
        if isinstance(engine, Engine):
            self.engine = engine

