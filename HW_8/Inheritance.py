# Створити клас який успадковується від класу з пункта 2. Додади для ініціалізації ще 1 параметр і ще один метод
# для виведення нового параметра.

# class Liquid:
#     def __init__(self, brand):
#         self.brand = brand
#     def print_brand(self):
#         print(f'The brand is {self.brand}')
from Init import Liquid

class New(Liquid):
    def __init__(self, brand, category):
        self.category = category
        super().__init__(brand)
    def print_category(self):
        print(f'The category is {self.category}')

    def print_category(self):
        print(f'The category is {self.category}')

a = Liquid('Brandy')
b = New('Brandy', 'Gin')


b.print_category()


