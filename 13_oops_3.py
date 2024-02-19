
# class, object, inheritance, encapsulation, polymorphism, abstraction.

# email = "username@gmail.com" # global

# def func():
#     global country
#     country = 'Bharat'


# func()
# print(country)


class Person:
    # public variables
    country = "Bharat"
    state = "Karnataka"
    # private variable
    __job = 'Labour'
    def __init__(self, name, age) -> None:
        # instance variables.
        self.name = name
        self.age = age
        print(Person.__job)

p = Person('shiv', 27)
# p2 = Person('Ganesh', 26)

# print(p.name, p.age, p.state, p.country)
print(Person.country, Person.state)


# public variables:
# 1. any variable declared inside of a class and outside of methods will be considered public variables.
# 2. any public variable can be accessed with object and classname as well.
# 3. this can accessible both inside and outside of class


# private variables:
# 1. any vairable declared inside of a class and outside of methods but naming convension starts with double underscore (__name) i.e private variable.
# 2. private variables can't be accessed outside of class
# 3. can be accessed inside of class.