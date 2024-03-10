# multi level inheritance.

# types:
# 1. single level
# 2. multi level
# 3. Hierarchial
# 4. multiple


# single level:
class A:
    def m1(self):
        print("A m1 method")


class B(A):
    def m2(self):
        print("B m2 method")


b = B()
b.m2()
b.m1()


# multi-level
class A:
    def m1(self):
        print("A m1 method")


class B(A):  # A
    # def m1(self):
    #     print('B m1 method')

    def m2(self):
        print("B m2 method")


class C(B):  # B, A
    def m3(self):
        super().m1()
        super().m2()
        print("C m3 method")


class D(C):  # A, B, C
    pass


# c = C()
# # c.m1()
# # c.m2()
# c.m3()

# a = A()
# a.m1()

# b = B()
# b.m2()
# b.m1()

# print(B.__mro__)

d = D()


# inheritance: the process of acquiring/accessing all the properties of super class to the child class is called inheritance.
# single level: only one level (grand father - father) (father -son) (son-grandson) (base - derived)
# single base class and single derived class

# multiple level: grand father -> father -> son -> grandson
# multi layer.
