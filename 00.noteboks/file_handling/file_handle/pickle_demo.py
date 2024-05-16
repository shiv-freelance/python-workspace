
# pickling -- take python object and write it to a file
# unpickling -- from a file read that object

from person import Person
import pickle

# pickle.dump(arg1, arg2): -- serialization
# arg1 -- object
# arg2 -- file path

# unpickling - deserailization.
# pickle.load(filepath)

# p = Person("Lakshman", 26, "lucky@gmail.com")

# print(p.name, p.age, p.email)

# with open('binary_objects.txt', mode='wb') as wfile:
#     pickle.dump(p, wfile)


with open('binary_objects.txt', mode='rb') as rfile:
    p1 = pickle.load(rfile)
    print(p1.name,p1.age, p1.email)
