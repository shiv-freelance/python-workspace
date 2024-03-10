# stmt = "Hare Krishna Hare rama"

# reverse a string
# print(stmt[::-1]) # entire string get reversed. (anhsirK eraH)

# output: eraH anhsirK
#         eraH anhsirK

# def reverse_string(string: str) -> str:
#     return string[::-1]

# wrd_lst = stmt.split()
# print(wrd_lst)
# result = ""

# for word in wrd_lst:
#     result = result + " "+reverse_string(word)

# print(result)


# get sum of previous, stop when enter 0.
nums = []
while True:
    num = int(input("enter the numebr"))
    if num == 0:
        break
    nums.append(num)

print(nums)
print(sum(nums))

# celsius to fahrenheit
C = 90
formula = f"{C}*(9/5)+32"

print(eval(formula))


# get second highest num in a list.
def get_highest_num(nums: list[int]):
    largest = nums[0]
    second_largest = nums[1]
    for i in range(2, len(nums)):
        if largest < nums[i]:
            largest, second_largest = nums[i], largest
        elif second_largest < largest and nums[i] > second_largest:
            second_largest = nums[i]

    return second_largest, largest


nums = [11, 2, 3, 9, 0, 7]
second_high, highest = get_highest_num(nums)
print("second highest: ", second_high)
print("highest in list is: ", highest)

# 2nd approach
# nums.sort()
# print(nums[-2]) # 2nd max
# print(nums[-1]) # highest
