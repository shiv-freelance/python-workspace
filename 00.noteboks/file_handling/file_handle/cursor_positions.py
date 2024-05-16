
"""
file modes:

1. read (r) -- read operation / write operations is not possible -- file should exist / if file is not there FileNotFoundError
2. write(w) -- write operation / read operation is not possible -- if file is not there it will create/ if it exists it will override existing content.
3. append(a) -- we append the content at last. -- read operation is not possible / write operation possible -- if file not existed it will create.
4. read&write (r+) -- here you can do both read and write operations. 
5. write & read (w+) -- Done
6. Append & read (a+) -- Assignemnt.
7. x - mode (exclusive)
"""

with open('india.txt', mode='r') as file:
    # print(file.read())
    print("cursor at: ", file.tell()) # tell() will give us the cursor position.
    print(file.read())
    print("#"*30)
    # change cursor position using seek() method.

    print(file.seek(5))
    print(file.read())
