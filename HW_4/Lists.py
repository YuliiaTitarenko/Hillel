# Створити простий список
import copy

original_list = [2, [1], 7, 8, 1]
print('\nOriginal list ID {}'.format(id(original_list)))
print('Original list[1] ID {}'.format(id(original_list[1])))
print('Original list: {}\n'.format(original_list))
# Створити змінну з посиланням на перший список
var_linked_to_list = original_list
print('Link to original list ID {}'.format(id(var_linked_to_list)))
print('Link to original list[1] ID {}'.format(id(var_linked_to_list[1])))
print('Link to original list: {}\n'.format(original_list))
# Створити поверхову (Shallow copy) копію першого списка
shallow_copy = copy.copy(original_list)
print('Shallow copy ID:{}'.format(id(shallow_copy)))
print('Shallow copy[1] ID:{}'.format(id(shallow_copy[1])))
print('Shallow copy: {}\n'.format(shallow_copy))
# Створити глибоку (повну) (Deep copy) першого списка
deep_copy = copy.deepcopy(original_list)
print('Deep copy ID: {}'.format(id(deep_copy)))
print('Deep copy[1] ID: {}'.format(id(deep_copy[1])))
print('Deep copy: {} \n'.format(deep_copy))
# Вивести значення всіх списків
print('***' * 15)
# Змінити перший список і ще раз вивести значення всіх списків
original_list.append(33)

print('\nOriginal list ID {}'.format(id(original_list)))
print('Original list[1] ID {}'.format(id(original_list[1])))
print('Original list: {}\n'.format(original_list))

print('Link to original list ID {}'.format(id(var_linked_to_list)))
print('Link to original list[1] ID {}'.format(id(var_linked_to_list[1])))
print('Link to original list: {}\n'.format(original_list))

print('Shallow copy ID:{}'.format(id(shallow_copy)))
print('Shallow copy[1] ID:{}'.format(id(shallow_copy[1])))
print('Shallow copy: {}\n'.format(shallow_copy))

print('Deep copy ID: {}'.format(id(deep_copy)))
print('Deep copy[1] ID: {}'.format(id(deep_copy[1])))
print('Deep copy: {} \n'.format(deep_copy))
print('_' * 60)

original_list[1].append(5)
print('\nOriginal list ID {}'.format(id(original_list)))
print('Original list[1] ID {}'.format(id(original_list[1])))
print('Original list: {}\n'.format(original_list))

print('Link to original list ID {}'.format(id(var_linked_to_list)))
print('Link to original list[1] ID {}'.format(id(var_linked_to_list[1])))
print('Link to original list: {}\n'.format(original_list))

print('Shallow copy ID:{}'.format(id(shallow_copy)))
print('Shallow copy[1] ID:{}'.format(id(shallow_copy[1])))
print('Shallow copy: {}\n'.format(shallow_copy))

print('Deep copy ID: {}'.format(id(deep_copy)))
print('Deep copy[1] ID: {}'.format(id(deep_copy[1])))
print('Deep copy: {} \n'.format(deep_copy))
