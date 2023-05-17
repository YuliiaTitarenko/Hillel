# створити список
fruits_list = ['banana', 'avocado', 'watermelon']
print('\nFruits list: {}'.format(fruits_list))
# копіювати через .copy()
list_of_fruits = fruits_list.copy()
print('\nList of fruits (copied): {}'.format((list_of_fruits)))
# додати елемент до списку
fruits_list.append('cherry')
print('\nAdd last element (append): ', fruits_list)
# вставити елемент а певне місце. (Задача на використання методу .insert(), говорив, але не встиг показати) (Задача з зірочкою*)
fruits_list.insert(0, "orange")
print('\nAdd first element (insert):', fruits_list)
# додати один список до іншого 2 способами *
fruits_list.extend(list_of_fruits)
print('\nAdd one list to another (extend)', fruits_list)
print('\nAdd one list to another (concatenate): ', fruits_list+list_of_fruits)
# команда .pop()
pop_element_first=fruits_list.pop(0)
print('\nRemove 1st element from the list (pop):', pop_element_first)
pop_element_last=fruits_list.pop()
print('Remove last element from the list (pop):', pop_element_last)
print('List after two removals', fruits_list)
# видалити елемент за значенням і за індексом.
fruits_list.remove('cherry')
print('\nRemove "cherry" element from the list:', fruits_list)
fruits_list.pop(0)
print('\nFruit list after element with index = 0 was removed:', fruits_list)
# показати як дістати значення елемента за його індексом.
print('\nShow the value of element with index = 1:', fruits_list[1])
