# Створити пустий словник одним з наведених в лекції способів
import copy

dictionary_1 = {}
print('Dictionary 1: {}'.format(dictionary_1))

# Створити новий словник з 2-3 парами ключ:значення
dictionary_car = {
  "brand": "Skoda",
  "model": "Scala"
}
print('\n1.Dictionary car: {}'.format(dictionary_car))

# Додати одну пару ключ:значення до першого словника
dictionary_1.update( {"colors": ["red", "white", "blue"]})
print('\n2.Dictionary car: {}'.format(dictionary_1))

# Додати до першого словника другий словник використовуючи .update()
dictionary_1.update(dictionary_car)
print('\n3.Updated dictionary 1: {}'.format(dictionary_1))

# видалити один елемент словника за допомогою .pop()
dictionary_1.pop('model')
print('\n4.Dictionary 1 with no model: {}'.format(dictionary_1))

# Видалити один елемент за допомогою .popitem()
dictionary_1.popitem()
print('\n5.Dictionary 2 with no colors: {}'.format(dictionary_1))

# Зробити глибоку копію першого словника в новgу змінну
new_dict = copy.deepcopy(dictionary_1)
print('\n6.New dictionary deepcopy: {}'.format(new_dict))

# Додати до нового словника новий ключ, а як значення передати перший словник
dictionary_car['key'] = dictionary_1
print('\n7.New dictionary with added key: {}'.format(dictionary_car))

# Вивести список ключів
key_list = dictionary_car.keys()
print('\n8.List of keys: {}'.format(key_list))

# Вивести список значень
value_list = dictionary_car.values()
print('\n9.List of values: {}'.format(value_list))