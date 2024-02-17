

# int, float, string, boolean, complex
# list, tuple, set, frozenset, dict

# int
# num = int(input('number: '))

# positive or negative
# if num < 0: 
#     print('negative number')
# else:print('positive number')

# primary
# def is_prime(num: int) -> bool:
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# if is_prime(num=num):
#     print('primary number')
# else:
#     print('it is not primary')


# nums: list[int] = [4, 4, 2, 6, 2, 6, 9, 0, 8]
# unique
# 1st approach
result = []
# for num in nums:
#     if num in result:
#         continue
#     else:
#         result.append(num)

# for num in nums:
#     if num in result:
#         continue
#     result.append(num)

# for num in nums:
#     if num not in result:
#         result.append(num)

#### not possible.
# output = [num for num in nums if num not in output]
# print(result)

# 2nd approach
# print(set(nums))


# xyz = 1,000,000
# print(xyz) # (1, 000, 000) (1000000) (1, 0, 0)

# x,y,z = 1,000,000 # x=1, y=0, z=0

# # x y z = 400 500 600 Error

# x_y_z = 1,000,000 # (1,0,0)
# print(x_y_z)

# x_y_z = 1_000_000 # 10000000
# print(x_y_z)



# numbers, enter 0 stop, i should be taking all the previous nums. i should get sum/avg

# for i in range(5) # will not work

# numbers = list()

# while True:
#     num = int(input('enter the number: '))
#     if num == 0:
#         break
#     numbers.append(num)

# # sum
# print("Sum is: ", sum(numbers))
# print("average: ", sum(numbers)//len(numbers))


nums: list[int] = [15, 4, 2, 6, 2, 6, 9, 0, 11]

# 1st approach
# print(max(nums))

def get_max_value(nums) -> int:
    max_value = nums[0]
    for i in range(1,len(nums)):
        if max_value < nums[i]: # 6 < 9; max_value = 6
            max_value = nums[i]   # max_value = 9

    return max_value

print(get_max_value(nums))   



