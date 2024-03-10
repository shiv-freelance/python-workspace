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
s2 = {5, 6, 2, 3, 9}

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
s2 = {5, 6, 2, 3, 9}

# AUB
# print(s1.union(s2)) # adding all values.
print(s1, s2)

print(s1.intersection(s2))  # common elements
print(s1, s2)

s1.intersection_update(
    s2
)  # common elements will be there in s1, remaining will be discarded.

print(s1, s2)

# https://byjus.com/maths/venn-diagrams/


lst = [1, 2, 3, 4]
print(lst[0])

t1 = (1, 2, 3, 4)
print(t1[0])

d1 = {"name": "Akshara"}

print(d1.get("name"))
print(d1["name"])


# fruits = ['apple', 'banana', 'strawberry', 'mango', 'orange']

# # fruits.sort(reverse=True) # reverse the list
# # fruits.sort() # by default it sorts based on first character of the word.

# fruits.sort(key=lambda x: x[1]) #it got sorted based on 2nd index position.
# print(fruits)


# result = (1, 2, 't', True, 3.4)
# # result.sort() # sorting is possible when a list contains only homogenous elements.
# print(result)

# nums = {1,2,3,4,5,1,2,3}


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.add(9)
# s1.difference_update(s2)
# print(s1.intersection(s2))
# s1.intersection_update(s2)
print(s1.isdisjoint(s2))  # no duplicates while joining the 2 sets.

s3 = {3, 4, 5, 6}
s4 = {4, 6, 5, 3}

print(s3.issubset(s4))  # checks all s3 elements present in s4 or not
print(s3.pop())
print(s1, s2)
print(s1.symmetric_difference(s2))

# print(s1.union(s2))

s1 = {1, 2, 3, 4}
s2 = {5, 6, 2, 3, 9}

print(s1.symmetric_difference(s2))
print(s1, s2)
s1.symmetric_difference_update(s2)
print(s1, s2)

s3 = {3, 4, 5, 6}
s4 = {4, 6, 5, 3, 9}

print(s3.issubset(s4))
print(s3.issuperset(s4))
print(s4.issuperset(s3))

print(s3.isdisjoint(s4))  # returns true if the intersection is null. (False)
s3 = {1, 2, 3, 4}
s4 = {5, 6, 7, 9}
print(s3.isdisjoint(s4))  # true
