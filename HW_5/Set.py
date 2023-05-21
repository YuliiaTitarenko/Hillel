## Створити set котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7
set_1 = {1, 2, 3, 4, 5, 6, 7}
print('\nset_1: {}'.format(set_1))
# Створити set котрий приймає в себе наступний ряд: 5, 6, 7, 8, 9, 10, 11
set_2 = {5, 6, 7, 8, 9, 10, 11}
print('\nset_1: {}'.format(set_2))
# Розширити перший сет за допомогою комaнди .add(0)
set_1.add(0)
print('\nset_1: {}'.format(set_1))
# Виконати команду .intersection() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
new_var_1 = set_1.intersection(set_2)
print('\nNew variable 1 (intersection): {}'.format(new_var_1))
# Виконати команду .difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
new_var_2 = set_1.difference(set_2)
print('\nNew variable 2 (difference): {}'.format(new_var_2))
# Виконати команду .symmetric_difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
new_var_3 = set_1.symmetric_difference(set_2)
print('\nNew variable 3 (symmetric_difference): {}'.format(new_var_3))