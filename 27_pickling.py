
# pickling:
#       we have python obj and we writing python obj to a file (serializing)

# unpickling:
#       reading the python obj from the file. (deserailizing)


from oops.person import Person
person1 = Person("Nagesh", 26, "nagesh@gmail.com")

# print(person1.name, person1.age, person1.mail)

print(person1)