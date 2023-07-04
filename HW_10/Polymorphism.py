# # 1.1 Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(), які виводять в консоль
# # відповідно, для методу wheels() - 4 та 8, а для методу mode_of_transport() -  "Private usage", "Public usage".
class Car:
    def wheels(self, wheels = 4):
        return wheels
    def mode_of_transport(self, mode_of_transport = 'Private usage'):
        return mode_of_transport

class Bus:
    def wheels(self, wheels = 8):
        return wheels
    def mode_of_transport(self, mode_of_transport = 'Public usage'):
        return mode_of_transport
#
# 1.2 Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом for по списку та викликати методи
# на кожному елементу списку.
car = Car()
bus  = Bus()

vehicles = [car, bus]
for vehicle in vehicles:
    print(vehicle.wheels(), vehicle.mode_of_transport())

print ('*'*30)

# 2. Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію.
# Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.

class Vehicle:
    def __init__(self, desc, wheels):
        self.desc = desc
        self.wheels = wheels
    def render(self):
        print(f'Vehicle desc: {self.desc}, with {self.wheels} wheels')
class Car(Vehicle):
    def __init__(self, desc, wheels):
        Vehicle.__init__(self, desc, wheels)

    def render(self):
        print(f'Car desc: {self.desc}, with {self.wheels} wheels')
class Bus(Vehicle):
    def __init__(self, desc, wheels):
        Vehicle.__init__(self, desc, wheels)

    def render(self):
        print(f'Bus desc: {self.desc}, with {self.wheels} wheels')

vehicle = Vehicle('Car\Bus', '4\8')
car = Car('a private automobile', 4)
bus = Bus ("for scheduled service", 8)
vehicle.render()
car.render()
bus.render()