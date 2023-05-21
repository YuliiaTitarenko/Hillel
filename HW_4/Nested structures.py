# 1) Створити 3 вимірний список (список 3х списків)
list = [8, 4, [7, 9, [5, 3], 1, 6], 2]
print('\n1.a) Three-dimensional list: {}\n'.format(list))
# Змінити, будь який, елемент, будь якого, спику.
list[3] = [1, 2 , 6]
print('1.b) Updated list (index # 3): {}\n'.format(list))


# 2) Створити словник зі вкладеним списком
dictionary_car = {
  "brand": "Skoda",
  "model": "Scala",
  "color": ["yellow", ["blue", "navy"], "green"]
}
print('2) Dictionary with nested list: {}\n'.format(dictionary_car))

#3) Створити список зі вкладеним словником
dictionary = {"name": "Yuliia",
              "occupation": "QA"
}
list_1 = ["House", dictionary]
print('3) List with added dictionary: {}\n'.format(list_1))

# 4) Зберегти вкладений список зі словника у нову змінну
var = dictionary_car.get("color")[1]
print('4) Var with nested list from dict: {}'.format(var))