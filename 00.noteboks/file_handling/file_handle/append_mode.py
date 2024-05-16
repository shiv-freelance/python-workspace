# when to use append

# file is existed, you don't want to loose previous content. you just want to add the content.

file = open('test2.txt', mode='a')

print(file.readable())
print(file.writable())

file.write('\nin this batch will discuss python, pytest, pandas, db')


file.close()
