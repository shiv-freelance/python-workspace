nums: list[int] = [0, 1, 5, 9, 10, 7, 3, 8]
target = 10
output = [(0, 10), (1, 9), (7, 3)]


for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i]+nums[j] == 10:
            print(nums[i],nums[j])
        # print(i, j)



# pivot integer
def pivotInteger(n: int) -> int:
    nums = list(range(1,n+1))
    size = len(nums)
    if size == 1:
        return n
    for i in range(1, size):
        left_vals = nums[:i]
        right_vals = nums[-1:-size+i:-1]
        if sum(left_vals) == sum(right_vals):
            return i
    return -1

pivotInteger(8)
############### (or) ##############
from math import sqrt

def pivotInteger(n: int):
    result = sqrt(n*(n+1)/2)
    return -1 if result % 1 != 0 else int(result)

