nums: list[int] = [0, 1, 5, 9, 10, 7, 3, 8]
target = 10
output = [(0, 10), (1, 9), (7, 3)]


for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        # if nums[i]+nums[j] == 10:
        #     print(nums[i],nums[j])
        print(i, j)
