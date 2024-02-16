
#operators

# 1. Arithemtic operator: +, -, *, /, //
# 2. comparision operator: ==, <, >, <=, >=
# 3. assignment operator: +=, -=, *=
# 4. membership operator: in, not in
# 5. identity operator: is, is not


# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2


print(3/2)
print(3//2)


result = 45
result = result + 5
result +=  5

print(result)


statement = "Ramu is a good child"
result = statement

print('god' not in statement)

print(id(statement), id(result))
print(id(statement) is id(result))

# = means assignment
# == means comparing equality

name = 'Akshara' # string Akshara assigned to a variable - name (= is a assignment operator)

print(10 == 10) # comparision