
# decorators:
#       adding additional functionality to the func or method is called decorator.

# 1. a fucntion as an input argument

# syntax:

# def decor_name(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper


# def div_decor(func):
#     def wrapper(a, b):
#         try:
#             return func(a, b)
#         except ZeroDivisionError:
#             print('division with zero is not possible')
#     return wrapper

# @div_decor
# def div(a, b):
#     return a/b


# print(div(10, 5))
# print(div(5, 0))

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"to execute '{func.__name__}' taken {time.time() - start} seconds")
    return wrapper

@timer
def test():
    time.sleep(5)
    print('test has been called!')

test()