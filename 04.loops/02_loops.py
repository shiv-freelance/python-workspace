# range()
# syntax: range(start=0, end-1, step=1)

result = range(100, 1000, 100)

print(result)
print(list(result))

# range(start=0, end-1, step=1);

# len() to get the length of the iterable.

# for loop
for value in range(2, 10, 2):
    print(value)


for char in "HareKrishna":
    print(char)


# while
num = 10
start = 0

while start < num:
    print(start)
    start = start + 1

# while True: # this is True always, will be infinite loop
#     print(83)

# while False: # never get's executed.
#     print('test')


# continue, break
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    if fruit == "mango":
        print("mango found!!!")
        break


for fruit in fruits:
    if fruit == "mango":
        continue
    print(fruit)
