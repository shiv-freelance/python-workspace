# oops:
# ----
#     1. class - blueprint
#     2. object - physical (no-class no-obj) - constructor
#     3. inheritance - super class - child class
#     4. encapusulation - setter and getter
#     5. polymorphism - overloading, overriding
#     6. Abstraction - hiding


# nums = [1, 2, 3, 4].append


# blueprint student.
class Student:
    # constructor
    def __init__(self, id, name, email) -> None:
        self.id = id
        self.name = name
        self.email = email

    def study(self):
        print(f"{self.name} is studying")

    # destructors
    def __del__(self):
        print("destructor")


# ref_name = ClassName(positional_args)
student1 = Student(1, "Shiv", "shiv@gmail.com")
del student1
# student2 = Student(2, 'Nagesh', 'shiv@gmail.com')
# student3 = Student(3, 'Aravind', 'shiv@gmail.com')
# student4 = Student(4, 'Ganesh', 'shiv@gmail.com')

# object_ref.property
print(student1.id, student1.name, student1.email)

# object.method_name()
# student1.study()
# student2.study()

# input()
# print()
# id()
# isinstance()
# len()
# int()
# float()
# str()
# bool()
