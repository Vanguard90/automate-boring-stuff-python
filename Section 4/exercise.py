def divide42(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide  by zero.')

print(divide42(2))
print(divide42(10))
print(divide42(0))
print(divide42(1))
