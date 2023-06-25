# Напишіть програму на Python для створення ланцюжка декораторів функцій (bold, italic, underline etc.):
# 1/Декоратор make_bold(fn) приймає функцію та повертає рядок який починається з відповідного тегу конкатенується із
# функцією та далі конкатенується з відповідним закриваючим тегом.
def make_bold(fn):
    def wrapper():
        return "<b>"  + fn() + "</b>"

    return wrapper
# 2/Декоратор make_italic(fn) приймає функцію та повертає рядок який починається з відповідного тегу конкатенується із
# функцією та далі конкатенується з відповідним закриваючим тегом.
def make_italic(fn):
    def wrapper():
        return "<i>"  + fn() + "</i>"

    return wrapper
# 3/Декоратор make_underline(fn) приймає функцію та повертає рядок який починається з відповідного тегу конкатенується
# із функцією та далі конкатенується з відповідним закриваючим тегом.
def make_underline(fn):
    def wrapper():
        return "<u>"  + fn() + "</u>"

    return wrapper
#   Результатом роботи, залежно від порядку декораторів, має бути подібний рядок - "<b><i><u>hello world</u></i></b>"
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"

print(hello())
