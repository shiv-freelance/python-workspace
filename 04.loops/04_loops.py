# range()
# syntax: range(start=0, end-1, step=1)

# result = range(100, 1000, 100)

# print(result)
# print(list(result))

# print('hello')


# operators:
# +, //, /, in, not in, is, is not

# operators
# arithemetic operators: add, subtract, mutliply, division, floor division
# comparision operators: <, >, <=,>=, ==
# assignment operators: =, +=, -=, *=, /= (result = result+10: result += 10)
# membership operators: in, not in
# identity operators: is, is not


# range(start=0, end-1, step=1);

# condition statements: if, else, elif

condition = False

# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')

# len() to get the length

# for loop

# import keyword
# print(len(keyword.kwlist)) getting all reserved keywords.


# for value in range(2, 10, 2):
#     print(value)


# for char in "Akshara":
#     print(char)

# while
num = 10
start = 0

# while start < num:
#     print(start)
#     start = start + 1

# while True: # this is True always, will be infinite loop
#     print(83)

# while False: # never get's executed.
#     print('test')


# continue, break
fruits = ["apple", "banana", "mango", "orange"]

# for fruit in fruits:
#     if fruit == "mango":
#         print("mango found!!!")
#         break


for fruit in fruits:
    if fruit == "mango":
        continue
    print(fruit)
