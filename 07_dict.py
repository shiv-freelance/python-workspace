
# dict
# key, value
# key is unique
# no insertion order

dt = {}
dt2 = dict()

print(type(dt), type(dt2))

dt: dict[dict] = {"student1":{"name": "Akshara", 'age': 27, 'mail': 'user@gmail.com',"name":"Subhash"}, 'student2': {}}

# print(dt)
# print(dt.keys())
# print(dt.values())

dt['student1']['age'] = 28 # mutable.
print(dt['student1']['mail'])
print(dt['student1'].get('age'))

# CURD; C-CREATE, U - UPDATE, R-READ, D-DELETE

# t1 = (1,2, 3)
# t1[0] = 10 # immutable
# print(t1[0])
# l1 = list(t1)
# l1[0] = 10
# print(l1)

