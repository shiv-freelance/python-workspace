# datastructures:
#   organizing the data in a better way. In python, we 5 different datastructures. They are,
#     1. list
#     2. tuple
#     3. set
#     4. frozenset
#     5. dict


# list
# 1. stores the values based on indexing
# 2. accepts both homogeneous and hetero
# 3. mutable
# 4. duplicates allowed.

# create a list
nums = []
nums = list()
print(type(nums))


# position vs indexing
nums = [1, 2, 3, 4, 5, True, 'name', 3.4, 2, 1, 2]

print(nums[6])
print(nums[-2])


# adding 
nums.append(False) # adds the element at last
print(nums)
nums.insert(0, 100) # inserts a value 100 at 0th index
print(nums)


count = nums.count(10)
print("2 present in list in {count} times".format(count=count))

print(nums[0])

del nums[0]
index = nums.index(2)
del nums[index]
print(nums)

print(len(nums))

fruits = ['apple', 'banana', 'mango', 'orange']

lst = [1,23,4]
lst.sort()
print(lst)

# new_fruits = fruits
# new_fruits.append('strawberry')

# # print(new_fruits)

# print(fruits)

# fruits = ['apple', 'banana', 'mango', 'orange']

# new_fruits = fruits.copy()
# new_fruits.append('strawberry')

# # print(new_fruits)

# fruits.append(new_fruits)

# print(fruits)


# nums1 = [1, 2, 3, 4, 5]
# nums2 = [6, 7, 8, 9, 10]

# nums2.extend(nums1)
# print(nums2)

# result = nums2+nums1

# print(nums1.pop(0)) # 5
# print(nums1) # [1, 2, 3, 4]

# nums2.sort()
# print(nums2)
# nums2.append('test')
# print(nums2)
# nums2.sort(reverse=True)
# print(nums2)

# fruits = ['apple', 'banana', 'strawberry', 'mango', 'orange']
# fruits.sort(key=lambda x: x[1])

# print(fruits)


# list comprehensions
#  where you are storing the data based on a conditional check, if condition get's sataisfied 
# then it stores the data into list.

# syntax: [item for item in iterable if conditional_check]

nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
even_list = []

for num in nums:
    if num % 2 == 0:
        even_list.append(num)
print(even_list)

even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)
