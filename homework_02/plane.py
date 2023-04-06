"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import  CargoOverload

class Plane(Vehicle):

    def __init__(self, weight:int, fuel:int, fuel_consumption:int, cargo=0, max_cargo=0):
        self.cargo = cargo
        self.max_cargo = max_cargo


print(Plane.__dict__)
