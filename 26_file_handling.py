
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
with open('students.txt', mode='a') as f:
    print(f.write("Nagesh\n"))
    print(f.write("Ganesh\n"))
    print(f.write("Rajesh\n"))
    print(f.write("Saif\n"))

# append, will add the data , it will not override existing data.
    