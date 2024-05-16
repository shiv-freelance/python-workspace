

with open('xyz.txt', 'w+') as file:
    # print(file.readable()) # True
    # print(file.writable()) # True
    print(file.tell()) # 0
    file.write('Yesterday\n we had Elections\n in India') # returns no.of character it written to a file.
    print(file.tell()) # 39

    print(file.read()) # nothing

    # move the cursor to 0
    file.seek(0)
    print(file.tell()) # 0

    print(file.read())

# with open('xyz.txt') as file:
#     print(file.tell()) # 0

#     print(file.read())

#     print(file.tell()) # 413
