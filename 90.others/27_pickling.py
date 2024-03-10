# pickling:
#       we have python obj and we writing python obj to a file (serializing)

# unpickling:
#       reading the python obj from the file. (deserailizing)


from oops.person import Person
import pickle

person1 = Person("Nagesh", 26, "nagesh@gmail.com")

# print(person1.name, person1.age, person1.mail)

# print(person1)

# load -> unpickle, dump --> pickling

# with open('persons_objs.txt', mode='wb') as file:
#     pickle.dump(person1, file)

#     print('pickling is Done!')

with open("persons_objs.txt", mode="rb") as file:
    up = pickle.load(file)
    print(up.name, up.age, up.mail)
