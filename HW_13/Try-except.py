# Створити конструкції try-except для арифметичної операції, роботи з колекціями.
try:
    a = 10
    b = 0
    print(a/b)
except Exception as ex:
    print(f'Caught DivisionByZeroError!: {ex}')
except ZeroDivisionError as e:
    print(f"Error: {e}")

print('=='*30)

try:
    my_list = [1, 2, 3]
    print('Fourth element in dictionary is:', (my_list[3]))
except Exception as exc:
    print(f'No such index: {exc}')
