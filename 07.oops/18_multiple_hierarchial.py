# hierarchial inheritance:
class A:
    def m1(self):
        print("A class: m1() method")


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


b = B()
b.m1()

c = C()
c.m1()

d = D()
d.m1()


# multiple inheritance:
#       a Single class extends(inherting) properties of multiple classes is called multiple inheritance.


class A:
    def m1(self):
        print("A m1() method")


class B:
    def m1(self):
        print("B m1() method")


class C(B, A):
    def m1(self):
        super().m1()
        print("C m1() method")


c = C()
c.m1()

# MRO - Method resolution order
print(C.__mro__)
