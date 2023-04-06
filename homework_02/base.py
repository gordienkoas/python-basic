from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=3):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel < self.fuel_consumption:
                raise LowFuelError

    def move(self, distance: int):
        required_fuel = distance * (self.fuel_consumption)
        fuel_now = self.fuel
        if fuel_now < required_fuel or fuel_now < self.fuel_consumption:
            raise NotEnoughFuel
        else:
            self.fuel -= required_fuel