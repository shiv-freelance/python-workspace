# print(help(dict))

# datastructures:
#     1. list
#     2. tuple
#     3. set
#     4. frozenset
#     5. dict


# datastructures:
# ---------------
#     organizing the data in better way.


# list

# 1. store: indexing
# 2. both homo, hetero
# 3. mutable
# 4. duplicates allowed.


# nums = []
# nums = list()
# print(type(nums))

# position vs indexing

# nums = [1, 2, 3, 4, 5, True, 'name', 3.4, 2, 1, 2]

# print(nums[6])
# print(nums[-2])

# nums.append(False)
# print(nums)
# # nums.insert(0)
# print(nums)

# count = nums.count(10)
# print("2 present in list in {count} times".format(count=count))

# print(nums[0])

# del nums[0]
# index = nums.index(2)
# del nums[index]
# print(nums)

# print(len(nums))

# fruits = ['apple', 'banana', 'mango', 'orange']

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
#  where you are storing the data based on a conditional check, if condition get's sataisfied then it stores the data into list.

# syntax: [item for item in iterable if conditional_check]

nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
# even_list = []

# for num in nums:
#     if num % 2 == 0:
#         even_list.append(num)
# print(even_list)

even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)
