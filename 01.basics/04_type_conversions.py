num = int("25")  # type conversion
print(num, type(num))

result = str(454545.34343)  # converting to string using str() function.
print(type(result))
print(complex(1))

# string to int
output = "0930xa9034"
print(int(output))  # fails it is alpha numeric.

# integer to float conversion.
result = 45
print(float(result))  # converting float using float() function


# float to int
result = 22 / 7
print(result, int(result))


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
