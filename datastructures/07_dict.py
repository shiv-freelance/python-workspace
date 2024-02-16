
# dict
# key, value
# key is unique
# no insertion order

# dt = {}
# dt2 = dict()

# print(type(dt), type(dt2))

# dt: dict[dict] = {"student1":{"name": "Akshara", 'age': 27, 'mail': 'user@gmail.com',"name":"Subhash"}, 'student2': {}}

# # print(dt)
# # print(dt.keys())
# # print(dt.values())

# dt['student1']['age'] = 28 # mutable.
# print(dt['student1']['mail'])
# print(dt['student1'].get('age'))

# CURD; C-CREATE, U - UPDATE, R-READ, D-DELETE

# t1 = (1,2, 3)
# t1[0] = 10 # immutable
# print(t1[0])
# l1 = list(t1)
# l1[0] = 10
# print(l1)

# keys()
# values()
# get()
# ["key"]
# adding element


dt1: dict = {"name": "Akshara", 'age': 27, 'mail': ['user@gmail.com', 'user1@gmail.com']}
dt2: dict = {"country": "Inida", "name": "Shiv"}


dt1.update(dt2)

# print(dt1)

# for key,value in dt1.items():
#     print(key, value, type(value))



# dict comprehension
# syntax: [item for item in iterable if condition] - list comprehension
# syntax: {item:value for item in iterable if condition} - dict comprehension
    
nums = [1, 2, 3, 4]

nums = (num*num for num in nums)
print(tuple(nums))

# nums = {num*num for num in nums} - set comprehension
# print(nums, type(nums))

# nums = {num: num*num for num in nums}
# print(nums, type(nums))