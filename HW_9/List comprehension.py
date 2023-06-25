# 1.Використовуйте list comprehension, щоб створити новий список, але додайте 6 до кожного елемента.
lst1 = [44, 54, 64, 74, 104]
lst2 = [x+6 for x in lst1] # місце для відповіді
print(lst2)

# 2. Використовуючи list comprehension, побудуйте список із квадратів кожного елемента в списку.
lst3 = [2, 4, 6, 8, 10, 12, 14]
list4 = [x**2 for x in lst3] # місце для відповіді
print(list4)

# 3. Дано словник який складається з транспортних засобів та їх маси в кілограмах. Складіть список назв транспортних
# засобів вагою до 5000 кілограмів. У тому самому list comprehension зробіть імена ключів великими регістром.
car_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
         "Motorcycle": 110}
# list5 = {k.upper():v for k,v in car_dict.items() if v < 5000}
list5 = [k.upper() for k, v in car_dict.items() if v < 5000] # місце для відповіді
print(list5)
