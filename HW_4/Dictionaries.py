# Створити пустий словник одним з наведених в лекції способів
import copy

dictionary_1 = {}
print('Dictionary 1: {}'.format(dictionary_1))
# Створити новий словник з 2-3 парами ключ:значення
dictionary_car = {
  "brand": "Skoda",
  "model": "Scala"
}
print('Dictionary car: {}'.format(dictionary_car))
# Додати одну пару ключ:значення до першого словника
dictionary_car.update( {"colors": ["red", "white", "blue"]})
print('Dictionary car: {}'.format(dictionary_car))
# Додати до першого словника другий словник використовуючи .update()
dictionary_1.update(dictionary_car)
print('Updated dictionary 1: {}'.format(dictionary_1))
# видалити один елемент словника за допомогою .pop()
dictionary_car.pop('model')
print('Dictionary with no model: {}'.format(dictionary_car))
# Видалити один елемент за допомогою .popitem()
dictionary_car.popitem()
print('Dictionary with no colors: {}'.format(dictionary_car))
# Зробити глибоку копію першого словника в новgу змінну
new_dict=copy.deepcopy(dictionary_1)
print('New dictionary deepcopy: {}'.format(new_dict))
# Додати до нового словника новий ключ, а як значення передати перший словник
new_dict.keys(dictionary_1)
print('New dictionary with added key: {}'.format(new_dict))
# Вивести список ключів
key_list = dictionary_car.keys()
print('List of keys: {}'.format(key_list))
# Вивести список значень
value_list = dictionary_car.values()
print('List of values: {}'.format(value_list))