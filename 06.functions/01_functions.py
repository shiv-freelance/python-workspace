# functions
# set of instrctions to perform a specific task in a block

# syntax:
#     def fun_name(arguments):
# return value

# syntax:
#     def fun_name(arguments):
# pass

import keyword

# print(keyword.kwlist) # 35

# method/function: def, pass, return


a = 20
b = 30.5

# def add(a: int, b: float) -> float:
#     sum = a+b
#     return sum

# def test():
#     print('inside test function')

# result = add(a,b)
# print(result)

# test()


def sub(a, b):
    return a - b


# a = 10
# b = 20
# print(sub(a, b)) # -10, b = 20, a = 10
# print(sub(b=b, a=a)) # 10, b = 20, a = 10

# Rules
# 1. it should be in same sequence.

# Arguments
# 1. positional arguments
# 2. keyword arg
# 3. default
# 4. variable length arg.


# 1. positional
# def sub(a, b):
#     return a-b

# a = 10
# b = 20
# print(sub(a, b)) # -10, b = 20, a = 10
# print(sub(b, a)) # 10, b = 20, a = 10


# # 2. keyword args:
# def sub(a, b):
#     return a-b

# a = 10
# b = 20
# print(sub(a, b)) # -10, b = 20, a = 10
# print(sub(b=b, a=a)) # -10, b = 20, a = 10


# # 3. default
# def hello(name="Bharat"):
#     return f"Hello, {name}"

# print(hello("nagesh"))
# print(hello())


# 4. variable length arguments.
nums = 1
nums = 1
# print(nums, type(nums))

# def test(a, b, c=10):
#     print(a, b, c)

# test(10, 20, 30) # 10, 20, 30
# test(10, 30) # 10, 30
# # test(10)

# *args-tuple


# def test1(*args):
#     print(args, type(args))


# test1(10, 20, 30, 40, 50, 60)
# test1(10)
# test1()


# # **kwargs - dict
# def sub(a, b):
#     return a-b

# a = 10
# b = 20
# print(sub(a, b)) # -10, b = 20, a = 10
# print(sub(b=b, a=a)) # -10, b = 20, a = 10


def test(**names):
    print(names, type(names))  # {'a':10, 'b': 20}, dict
    for key in names.keys():  # keys
        print(key)
    # this for loop prints all values
    for value in names.values():
        print(value)

    for key, value in names.items():  # key, value
        print(key, value)

    for item in names.items():  # tuple
        print(item, type(item))


# test(a = 10)
# test(a=19, c=100)

test()
