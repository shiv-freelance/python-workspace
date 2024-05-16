# when you are opening a file in Exclusive mode - file should not exist
# if file exists -- Error: FileExistError
# file doesn't exist -- it will create.

with open('xyz.txt', mode='x') as file:
    print(file.readable())
    print(file.writable())



# r -- file not exist -- FileNotFoundError
# w - file not exist -- I will created one.
# a - file not exist -- I will create one.
# r+ -- file not exist -- FileNotFoundError
# w+ -- file not exist -- I will create one
# a+ --
# x -- file not exist -- I will create 
