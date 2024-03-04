

def dec(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            print('division with zero is not possible')
    return wrapper

@dec
def div(a, b):
    return a/b


print(div(10, 0))