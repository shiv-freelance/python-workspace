
# polymorphism:
#   poly - many forms

# overloading, overriding

# overriding: once a method has been overridden you can have your own functionality. (method signature should be same.)

class A:
    def m1(self, a, b):
        print(a+b)

class B(A):
    def m1(self, a, b):
        print(a, b)

b = B()
b.m1(5, 5)

a = A()
a.m1(5, 5)


# overloading:
class Person:
    # def __init__(self, name):
    #     print('arugment has been passed, ', name)

    def __init__(self):
        print('zero arg constructor')

    # def test(self):
    #     print('zero test method')

    def test(self, a):
        print('i am having extra arg', a)

p1 = Person() # zero arg constructor
# p2 = Person('shiv')

p1.test(6)