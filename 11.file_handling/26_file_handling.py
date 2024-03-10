# files:
#       1. text  2. binary

# text  ==> .txt
# binary ==> images, videos, pdfs

# storages:
#       temp, perm

# temp: all ds, variables

# permamnenet storage location ===> files, databases.


# 1. opening 2. read/write  3. close


# # opening
# f = open("students.txt")

# # read/write
# print(f.read())

# # close
# f.close()

# file_path = input('enter the file path: ')

# with open(file_path) as f:
#     print("file name: ", f.name)
#     print('file mode: ', f.mode)
#     print("file is closed or not: ", f.closed)
#     print("file is readable or not ", f.readable())
#     print('file is writable or not: ', f.writable())

# print("file is closed or not: ", f.closed)
# if python file and text file in same folder, file name is enough.
# if python file and text file in diff location, you should specify full path.


# modes:
# 1. read = r
# 2. write = w
# 3. append = a
# 4. read and write = r+
# 5. write and read = w+
# 6. append and read = a+
# 7. exclusive == x

# 1. read
# with open('students.txt', mode='r') as f:
#     print(f.read())

# 2. write
# with open('students.txt', mode='w') as f:
#     print(f.write("Aravind"))

# write case: if file is there write it, if file is not exists it will create one.
# in write: file will always overridden.

# 3. append
# with open('students.txt', mode='a') as f:
#     print(f.write("Nagesh\n"))
#     print(f.write("Ganesh\n"))
#     print(f.write("Rajesh\n"))
#     print(f.write("Saif\n"))

# append, will add the data , it will not override existing data.


# Note: when you are doing a write operation, until your file close the data will not be written.

# f = open('dummy.txt', mode='w')

# f.write('hello\n')
# f.write('good\n')
# f.write('morning!\n')

# f.close()

# 4. read and write (r+)

# with open('dummy.txt', mode='r+') as f:
#     print(f.read())
#     print(f.tell())
#     f.write('new data\n')


# to know cursor position, we have 2 methods. seek(), tell()

# 1. tell(): tell me the cursor postion
# 2. seek(): will take you to the specified index position


# 5. write and read (w+):
# with open('dummy.txt', mode='w+') as f:
#     print(f.tell())
#     f.write('new data\n')
#     print(f.tell()) # cursor position.
#     f.write('cursor check\n')
#     print(f.tell())
#     if f.tell() != 0:
#         f.seek(3)
#     print(f.read())

# 6. append and read(a+):
# with open('dummy.txt', mode='a+') as file:
#     print(file.tell())
#     file.seek(0)
#     print(file.read())
#     # file.write('append+ check\n')


# 7. Exclusive (X)
# with open('dummy1.txt', mode='x') as file:
#     file.write('test data of x mode.')
#     # print(file.readable())
#     # print(file.read())
#     if file.readable():
#         print(file.read())
#     else:
#         print('file canot be readable.')


# binary
# rb, wb, ab, r+b, w+b, a+b, xb

# creating copy of the image.
# with open('student-class.jpg', mode='rb') as file:
#     with open('student-img.jpg', mode='wb') as wfile:
#         wfile.write(file.read())

# text files
with open("setup.txt", mode="r") as rfile:
    with open("setup-copy.txt", mode="w") as wfile:
        wfile.write(rfile.read())
