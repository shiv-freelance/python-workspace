# file = open('test1.txt', mode='r+')


# file.close()

with open('test1.txt', mode='r+') as file:

    print(file.write('I am just doing write operation\n'))
