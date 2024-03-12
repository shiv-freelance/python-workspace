
# 5 fundamental data types:

# 1. int
# 2. float
# 3. string
# 4. boolean
# 5. complex

# type conversions: Convert from one datatype to another datatype
# ex: int -> float; boolean -> int

# type conversion functions:

# 1. int(value): value the one which needs to converted to int
# 2. float(value)
# 3. string(value)
# 4. bool(value)
# 5. complex(value)

decimal:float = 34.98
flag: bool = True
string_val:str = 'Siddhu'
int_val:int = 100
complex_val: complex = 10+30j #a+ib

# int conversion
int(decimal) # 34
int(flag) # 1
int(False) # 0
int(string_val) # ValueError (if it's digits it get's converted)
num = int("25")  # get's converted.
print(num, type(num))
# float to int
result = 22 / 7 # 3.14
print(result, int(result)) # 3


# float conversion
float(100) # 100.0
float(True) # 1.0
float(False) # 0.0


# String conversion; any value passed as an arguemnt get's converted to string datatype
result = str(454545.34343)  # converting to string using str() function
print(type(result)) # checking the datatype using type() function
# string to int
output = "0930xa9034"
print(int(output))  # fails it is alpha numeric.


# complex datatype
print(complex(1))
complex(8, 10) # 8+10j


# boolean conversion
flag1 = True
type_conversion = bool(" ")
print(type_conversion)
print(flag1, int(True), int(False))



# string to int
value = "90"  # string

# isinstance(obj, class) ==> Return whether an object is an instance of a class or of a subclass thereof.
if isinstance(value, str):  # to check the datatype is matching or not.
    value = int(value)  # type conversion

print(value, type(value))
