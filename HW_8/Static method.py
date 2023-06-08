# Додати до класу з пункту 2 змінну класу та статичний метод.
class Liquid:
    def __init__(self, brand, category):
        self.brand = brand
        self.category = category

    def print_brand(self):
        print(f'The brand is {self.brand}')

    vodka = 'Absolut'
    @staticmethod
    def new_var():
        print(Liquid.vodka)


Liquid.new_var()
