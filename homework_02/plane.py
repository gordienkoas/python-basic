"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self,
                 weight: int,
                 fuel: int,
                 fuel_consumption: int,
                 max_cargo=int):
        super().__init__()
        self.cargo = 0
        self.max_cargo = max_cargo
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.weight = weight

    def load_cargo(self, added_load: int):
        if self.cargo + added_load <= self.max_cargo:
            self.cargo += added_load
        else:
            raise CargoOverload

    def remove_all_cargo(self) -> int:
        result = self.cargo
        self.cargo = 0
        return result
