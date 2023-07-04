# 1. Створити файл та записати в нього рядок.
f = open('new.txt', 'w')
f.write('New line')
f.close()

# 2. Прочитати створений файл та вивести на консоль вміст файлу
f = open('new.txt', 'r')
print(f.read())
f.close()

# 3. Додати ще один рядок до створеного файлу.
with open('new.txt', 'a') as f:
    f.write('\nSecond line')


# 4. Прочитати всі рядки з файлу та вивести на консоль.
with open('new.txt', 'r') as f:
    print(f.readlines())
# 5. Записати у файл все щo користувач введе з консолі. (Якщо хочете більш ніж один рядок спробуйте використати
# while True і перевірку на введений рядок, типу якщо exit тоді це кінець.)
strings = []
while True:
    string = input('>')
    if string == 'exit':
        break
    strings.append((string + '\n'))
with open('New_file.txt', 'w') as f:
    f.writelines(strings)
