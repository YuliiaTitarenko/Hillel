# 1.побітове AND:
# 1.1Порівняти два різних цілих і два однакових числа і вивести результат
print('\n1.1 Bitwise AND for different numbers: {}'.format(bin(100 & 150)))
print('\n1.2 Bitwise AND for equal numbers: {}'.format(bin(100 & 100)))

# 1.2 Порівняти два різних рядка і два однакових рядка і вивести результат
a = "t1"
a_bytes = a.encode('utf8')
b = "t2"
b_bytes = b.encode('utf8')
c = "test"
c_bytes = c.encode('utf8')

for x in a_bytes:
    for y in b_bytes:
        print('\n1.3 char from a_bytes = {0:b}, char from b_bytes = {1:b}. Bitwise AND = {2:b}'.format(x, y, x & y))

for x in a_bytes:
    for y in c_bytes:
        print('\n1.4 char from a_bytes = {0:b}, char from с_bytes = {1:b}. Bitwise AND = {2:b}'.format(x, y, x & y))

# 2.Повторити дії і та іі з пункту а для решти операцій (OR, XOR, NOT)
print('\n2.1 Bitwise OR for different numbers: {}'.format(bin(100 | 150)))
print('\n2.2 Bitwise OR for equal numbers: {}'.format(bin(100 | 100)))
print('\n2.3 Bitwise XOR for different numbers: {}'.format(bin(100 ^ 150)))
print('\n2.4 Bitwise XOR for equal numbers: {}'.format(bin(100 ^ 100)))
print('\n2.5 Bitwise NOT for 150: {}'.format(bin(~ 150)))

for x in a_bytes:
    for y in b_bytes:
        print('\n2.6 char from a_bytes = {0:b}, char from b_bytes = {1:b}. Bitwise OR = {2:b}'.format(x, y, x | y))

for x in a_bytes:
    for y in c_bytes:
        print('\n2.7 char from a_bytes = {0:b}, char from с_bytes = {1:b}. Bitwise OR = {2:b}'.format(x, y, x | y))

for x in a_bytes:
    for y in b_bytes:
        print('\n2.8 char from a_bytes = {0:b}, char from b_bytes = {1:b}. Bitwise XOR = {2:b}'.format(x, y, x ^ y))

for x in a_bytes:
    for y in c_bytes:
        print('\n2.9 char from a_bytes = {0:b}, char from с_bytes = {1:b}. Bitwise XOR = {2:b}'.format(x, y, x ^ y))

for x in a_bytes:
    print('\n2.10 char from a_bytes = {0:b}. Bitwise NOT for "t1" {1:b}'.format(x, ~x))



# 3.Виконати побітовий зсув вліво для:
# 3.1Цілого числа на 1, 2 та 3 біти
print('\n3.1 Побітовий зсув вліво "100" на 1: {}'.format(bin(100 << 1)))
print('\n3.2 Побітовий зсув вліво "100" на 2: {}'.format(bin(100 << 2)))
print('\n3.3 Побітовий зсув вліво "100" на 3: {}'.format(bin(100 << 3)))

# 3.2Рядка на 1, 2 та 3 біти
for x in a_bytes:
    print('\n3.4 char from a_bytes = {0:b}. Bitwise left shift 1 for "t1": {1:b}'.format(x, x << 1))

for x in a_bytes:
        print('\n3.5 char from a_bytes = {0:b}. Bitwise left shift 2 for "t1": {1:b}'.format(x, x << 2))

for x in a_bytes:
    print('\n3.6 char from a_bytes = {0:b}. Bitwise left shift 3 for "t1": {1:b}:'.format(x, x << 3))

# 4.Виконати побітовий зсув вправо для:
# 4.1Цілого числа на 1, 2 та 3 біти
print('\n4.1 Побітовий зсув вправо "100" на 1: {}'.format(bin(100 >> 1)))
print('\n4.2 Побітовий зсув вправо "100" на 2: {}'.format(bin(100 >> 2)))
print('\n4.3 Побітовий зсув вправо "100" на 3: {}'.format(bin(100 >> 3)))

# # 4.2Рядка на 1, 2 та 3 біти

for x in a_bytes:
    print('\n4.5 char from a_bytes = {0:b}. Bitwise right shift 1 for "t1": {1:b}'.format(x, x >> 1))

for x in a_bytes:
        print('\n4.6 char from a_bytes = {0:b}. Bitwise right shift 2 for "t1": {1:b}'.format(x, x >> 2))

for x in a_bytes:
    print('\n4.7 char from a_bytes = {0:b}. Bitwise left right shift 3 for "t1": {1:b}'.format(x, x >> 3))
