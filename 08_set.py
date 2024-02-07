# list = [], list()
# tuple = (), tuple()
# set = set()
# frozenset = frozenset()
# dict = {}, dict()

# value = ("string",)
# print(value, type(value))


# lst: list[int] = [1,4,5,9, 4]

# # print(lst[10]) -- indexError
# # print(lst.index(10)) -- ValueError

# print(lst.count(10)) #0
# print(lst.count(4)) # 2

# set
# no-insertion
# indexing
# duplicates
# mutable

# s1 = set()
# s1 = {10,2,9, 3, 1, 2, 100}
# print(s1, type(s1))
# s1.add(99)
# print(s1)

# s1.add(9)

# s1.clear()
# print(s1)

s1 = {1, 2, 3, 4}
s2 = {5, 6, 2, 3,9}

# s2.add(9) # {4, 5, 6, 7, 9}
# print(s2)
# s1.difference(s2) # {1, 4}
# print(s1, s2)
# s1.difference_update(s2)
# print(s1, s2)

# # s1.remove(40) -- keyError
# # s1.discard(40) -- there or not, if there then remove, if not ignore
# s1.discard(2)
# print(s1)

# print(s2)
# print(s2.pop()) -- removes and returns
# print(s2)

s1 = {1, 2, 3, 4}
s2 = {5, 6, 2, 3,9}

# AUB
# print(s1.union(s2))
print(s1, s2)

print(s1.intersection(s2))
print(s1, s2)

s1.intersection_update(s2)

print(s1, s2)
