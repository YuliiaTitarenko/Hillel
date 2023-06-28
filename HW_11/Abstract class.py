# 1. Створити клас з абстрактним методом. Створити об'єкт даного класу.
from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def go (self):
        pass

_vehicle = Vehicle()

# 2. Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.

class Vehicle2(ABC):
    @abstractmethod
    def go (self):
        pass
vehicle2 = Vehicle2()

# 3. Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від абстрактного класу і
# створіть об'єкт нового класу.
class Vehicle3:
    @abstractmethod
    def go (self):
        pass

class New(Vehicle3):
    def go (self):
        print("Inherited class")

new_veh = New()
new_veh.go()