# За допомогою даної конструкції перевернути рядок
row = 'Lorem ipsum dolor sit amet'
print('\nRow:{}'.format(row))
row1 = row[::-1]
print('Reverted row: {}\n'.format(row1))
# За допомогою даної конструкції перевернути список

number_list = [1, 2, 3, 4, 5, 7, 8, 9, 10]
print('Number list: {}'.format(number_list))
revert_list = number_list [::-1]
print('Reverted list: {}\n'.format(revert_list))

# повернути частину списку від 2 до 7 елементу з кроком 2
part_list_2_7 = number_list[2:7:2]
print('Part of list from 2 to 7 element with step 2: {}\n'. format(part_list_2_7))

# повeрнути частину рядка (вважати рядок списком)
row_len = len(row)
half_list = row [0:13:1]
print('Row length: {}'.format(row_len))
print('Half of the list: {}'.format(half_list))