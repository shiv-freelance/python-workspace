file = open('check1.txt', mode='w') # it will check file exist or not, file exists it will override the content. 
# if file is not there then it will create one.

file.write('latest update content')

print(file.readable())

print(file.read())

file.close()