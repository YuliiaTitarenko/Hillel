# Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно. /
#Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями. (35 балів)

def sum_range(start, end):
    if start > end:
        temp_var = start
        start = end
        end = temp_var
    result = 0
    if 0 in (start, end):
        return -1
    return int(end*(end+1)/2-start*(start+1)/2)+start

a = [3, 1, 4, 5, 6]

sum_range(a)