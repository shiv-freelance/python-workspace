
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
int_value = 10  # there is no size capacity
float_value = 20.854985  # no double type
bool_val = True  # True/False statement
complex_val = 2+3j # it's denoated as a+ib format
str_value = 'I am String'  # String can be denotated with either single/double Quote (no char type in python)


# int
result = 98

value = "90" # string

if isinstance(value, str):
    value = int(value) # type conversion

print(result, type(result))
print(value, type(value))



result = 15_00_00_000
print(result)


_ = 3+4
print(_)




# float
result = 45.999
print(int(result)) # converting int, using int() function

result = 45
print(float(result)) # converting float using float() function



# boolean
result = True
output = False

type_conversion = bool(" ")

print(type_conversion)
print(result, int(True), int(False))



# string
result= 'apple'
statement = "ramu is a good child"
statement = """Ramu is
a 
good
child"""

print(statement) # printing a multi-line string


result = str(454545.34343) # converting to string using str() function.
print(type(result))
print(complex(1))