# Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно. /
#Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями. (35 балів)

def sum_range(start, end):
    if start > end:
        temp_var = start
        start = end
        end = temp_var
    print(sum(range(start, end +1 )))

sum_range(1, 10)