# Datatypes:
#         numbers: int, float
#         boolean: True, False
#         strings: '', "", """triple quote"""
#         complex: a+bj; a-real and b-img


"""
Fundamental Data Types in Python
--------------------------------

1. Strings - "Revanuru"
2. Integers - 45
3. Floats - 3.14
4. Boolean - True/False
5. Complex - a+bj: a = real, b = imaginary
"""


# In python semicolon is Optional at the end of statement
# Fundamental Datatypes
int_value: int = 10  # there is no size capacity
float_value: float = 20.854985  # no double type
bool_val: bool = True  # True/False statement
complex_val: complex = 2 + 3j  # it's denoated as a+ib format
str_value: str = (
    "I am String"  # String can be denotated with either single/double Quote (no char type in python)
)


# int
count = 10
print(count)

num = 98
print(num, type(num))

amount = 1, 50, 00, 00, 000
print(amount)

flag1 = 15_00_00_000
print(flag1)

# *****************************#

# float
flag1 = 45.999
print(int(flag1))  # converting int, using int() function


# *****************************#

# boolean
flag1 = True
flag2 = False


# *****************************#

# string declaration
test: str = "test"
print(test)

flag1 = "apple"
statement = "ramu is a good child"
statement = """Ramu is
a 
good
child"""

print(statement)  # printing a multi-line string
