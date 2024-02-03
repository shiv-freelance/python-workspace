
#operators

# 1. Arithemtic operator: +, -, *, /, //
# 2. comparision operator: ==, <, >, <=, >=
# 3. assignment operator: +=, -=, *=
# 4. membership operator: in, not in
# 5. identity operator: is, is not


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
