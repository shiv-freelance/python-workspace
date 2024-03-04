

def m1():
    return 10, 29, 'shiv'
    # return 29
    # return 'shiv' >>> dead code

# print(m1())

# list comprehension
# num_lst = [i for i in range(10) if i < 10]

# set comprehension
# set_val = {i for i in range(10) if i < 10}

# # dict comprehension
# dict_val = {i: i*i for i in range(10) if i < 10}

# print(num_lst)
# print(set_val)
# print(dict_val)

# num_lst = (i for i in range(10) if i < 10)
# print(list(num_lst))

# import sys

# nums = [i for i in range(1000000)]
# nums_gen = (i for i in range(1000000))

# print(sys.getsizeof(nums))
# print(sys.getsizeof(nums_gen))

# # print(nums)
# # print(next(nums_gen)) # 0
# # print(next(nums_gen)) # 1
# # print(next(nums_gen)) # 2

# for _ in range(500000):
#     next(nums_gen)

# print(sys.getsizeof(nums_gen))

# nums = (i for i in range(10))
# print(list(nums))
# print(list(nums))


def new_generator():
    yield 1
    yield 2
    yield 3

gen = new_generator()

try:
    print(next(gen))
    print(next(gen))
    print(list(gen))
    print(next(gen))
except StopIteration:
    print('you reached end of the generator')

# for i in gen:
#     print(i)

# print(next(gen))
# print(next(gen))
# print(next(gen))
    
# for i in range(3):
#     print(next(gen))

# print(gen)
# print(list(gen))

# 1. a generator can be created using yield keyword.
# 2. if you want access either you can iterate it, or use next()
# 3. once all values iterated, generator will be empty
# 4. once it is empty you try to use next(), you will get StopIteration


# fibonacci series.

# def fibonacci(num):
#     a = 0
#     b = 1

#     while a < num:
#         yield a
#         # a, b = b, a+b
#         temp = b
#         b = a+b
#         a = temp

# # 100 
# print(tuple(fibonacci(100)))
# (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)


# custom range

# range; start, end, step=1

# def shiv_range(start, end, step=1):
#     while start < end:
#         yield start
#         start = start + step

# # result = shiv_range(1, 11)
# result = shiv_range(0, 11)

# # for i in result:
# #     print(i)

# print(result)
# print(tuple(result))

# print(range(0, 11))

# for i in range(100):
#     print(i, end=' ')

