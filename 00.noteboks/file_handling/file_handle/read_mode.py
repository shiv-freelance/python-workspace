
file = open(file="india.txt", mode='r') # file should be existed, if not FileNotFoundError
# print(file.name)
# print(file.readable())
# print(file.writable())
# print("before closing", file.closed)
# file.close()
# print("after closing", file.closed)

# when file opened in read mode, you can do only read operation.

# print(file.read()) # reads entire file content.

# print(file.read(20)) # space is also character

# print(file.read(50))

# print(file.readline())

# print(file.readlines())

lines = file.readlines()

# for line in lines:
#     print(line)

for line in lines:
    if "has" in line: # membership operators.
        print(line)