
a: int = int(input('first value: '))
b: int = int(input('second value: '))

print(a+b)

for i in range(50):
    print(i, end=' ')

# write a program to print from 1000 to 1010
for i in range(1000, 1010, 1):
    print(i, end='\t')

# even numbers
nums = [2,6,34,32,11, 9, 15, 22]

for i in nums:
    if i % 2 != 0:
        print(i)

for i in range(len(nums)):
    print(i, nums[i])


fruits = ['apple', 'banana', 'mango', 'orange']

for fruit in fruits:
    if 'e' not in fruit:
        print(fruit)
    elif 'a' not in fruit:
        print(fruit)

value = -10

if value < 15 and value > 0:
    print('inside if')
else:
    print('else block')