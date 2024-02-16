nums = []

while True:
    num = int(input('enter the numebr'))
    if num == 0:
        break
    nums.append(num)

print(nums)
print(sum(nums))