
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
    return a-b

a = 10
b = 20
print(sub(a, b)) # -10, b = 20, a = 10
print(sub(b=b, a=a)) # 10, b = 20, a = 10

# Rules
# 1. it should be in same sequence.

# Arguments
# 1. positional arguments
# 2. keyword arg
# 3. default
# 4. variable length arg.


#1. positional
def sub(a, b):
    return a-b

a = 10
b = 20
print(sub(a, b)) # -10, b = 20, a = 10
print(sub(b, a)) # 10, b = 20, a = 10


# 2. keyword args:
def sub(a, b):
    return a-b

a = 10
b = 20
print(sub(a, b)) # -10, b = 20, a = 10
print(sub(b=b, a=a)) # -10, b = 20, a = 10


# 3. default
def hello(name="Bharat"):
    return f"Hello, {name}"

print(hello("nagesh"))
print(hello())