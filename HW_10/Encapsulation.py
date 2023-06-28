# Створити клас з 2 змінними (_a and __a), Створити об'єкт класу та показати доступ до цих змінних.
class Klass:
    def __init__(self, a1, a2):
        self._a = a1
        self.__a = a2

    def get_private_a(self):
        return self.__a

x = 1
y = 2

obj1 = Klass(x, y) # instance of class Klass (object)
obj2 = Klass(33, 44)

print(obj1._a, obj1.get_private_a())
print(obj2._a, obj2.get_private_a())
