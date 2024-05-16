# file = open('india.txt') # in a read mode file immutable

# # print(file.name)
# # print(file.mode)
# # print(file.readable())
# # print(file.writable()) # False
# # print(file.closed)
# # print(file.close()) # closing a file
# # print(file.closed)

# print(file.read()) # once you close a file and try read it (Unsupported Operation: performing read on a closed file.)


#note: in a read mode if file not exist you will FileNotFoundError

# write
# file = open('abc.txt', mode='w') #note: in a write mode if file not exist you will a new file will be created.

# print(file.writable()) # True -- write permissions (write -- file mutable.)
# print(file.readable()) # False -- readable.

# # print(file.read()) - can't perform read operation, when file opened in write mode.

# file.write("once you close a file and try read it (Unsupported Operation: performing read on a closed file")

# file.close()

# print('file is written!!!')


# file = open('dummy.txt', mode='r') # immutable
# # file.write('i am write operation')
# print(file.read())



file = open('check.txt', mode='w') # mutable
# file.write('i am write operation')
print("file is created....")
print(file.read()) # on write you can't perform read operation

