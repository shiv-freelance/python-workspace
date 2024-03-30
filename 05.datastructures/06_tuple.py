# tuple
t1 = (1, 2, 3, 4, 3)
t2 = tuple()

print(type(t1))
print(type(t2))

# t1[0] = 10

print(t1.index(4))
print(t1.count(30))
print(t1[3])

even_nums = (num for num in t1 if num % 2 == 0)
print(tuple(even_nums), type(tuple(even_nums)))

# print(len(t1))
# print(max(t2))
# print(min(t2))
