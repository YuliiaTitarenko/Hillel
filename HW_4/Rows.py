# Навести приклад простого рядка
row = ' Ой у лузі червона калина похилилася.'
print('\nSimple row: {}'.format(row))

# Навести приклад багаторядкового рядка (Вірш, хоку - щоб показати форматування)
multilinerow = '''
Нічної хвилі хлюпіт об весло.
Нутро холоне,
Сльози набігають.'''
print('\nMultiline  row: {}\n'.format(multilinerow))

# Навести приклад рядка з ігноруванням екрануючих символів (Raw)
raw_row = R'C:\Users\yuliia\Downloads'
print('Raw string: {}\n'.format(raw_row))

# Навести приклад форматування довгих рядків
format_long_rows = 'Ice Apple, the first on our list of fruits that start with the letter ‘I’, is scientifically ' \
                   'known as Borassus Flabellifer and is a jelly-like fruit, similar to litchi.' \
                   'The skin is a bit hard to protect the soft flesh inside that is quite delicate to touch and holds' \
                   'a translucent fluid inside.\n '
print('Long string in 1 row: {}'.format(format_long_rows))
readable_format = '   Ice Apple, the first on our list of fruits that start with the letter ‘I’, is scientifically \n' \
                   'known as Borassus Flabellifer and is a jelly-like fruit, similar to litchi.\n' \
                   'The skin is a bit hard to protect the soft flesh inside that is quite delicate to touch and holds\n' \
                   'a translucent fluid inside. '
print('Readable long string: {}'.format(readable_format))
