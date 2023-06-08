# Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр
class Liquid:
    def __init__(self, brand):
        self.brand = brand

    def print_brand(self):
        print(f'The brand is {self.brand}')

a = Liquid('Brandy')


a.print_brand()
