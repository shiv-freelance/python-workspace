fruits = ["apple", "mango", "strawberry", "orange"]
# iterator

# iterable
#       which can be iterated.

# for i in tuple(fruits):
#     print(i)

# string: group/ sequence of characters

# for i in "India":
#     print(i)

# print(dir(list))

# nums = [1, 2, 3, 4 ,5]

# for i in nums:
#     print(i)

# num_dict = {1:100, 2: 200, 3: 300, 4: 400}

# print(dir(num_dict))

# for i in num_dict.items():
#     print(i)

fruits = ["apple", "mango", "strawberry", "orange"]

# for i in fruits:
#     print(i)

# for i in range(len(fruits)):
#     print(i, fruits[i])

for index, value in enumerate(fruits):
    print(index, value)
