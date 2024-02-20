
# public and private
# instance, class, static

class Test:
    # public variables.
    sub1 = "English"
    sub2 = "Maths"

    def __init__(self, sub1_marks, sub2_marks) -> None:
        # instance variables.
        self.sub1_marks = sub1_marks
        self.sub2_marks = sub2_marks
        self.dummy()

    # instance method
    def info(self):
        print("I am instance method")
        print(self.sub1_marks)
        self.dummy()
    
    # class method
    @classmethod
    def class_method_test(cls):
        print('class method')
        # print(self.sub1_marks)


    #static method
    @staticmethod
    def info3():
        print("I am static method")
        # print(self.sub1_marks)
    
    def dummy(self):
        print("I am display method")

    


# Test.info3()

t1 = Test(90, 99)
# t1.info3()
t1.info()
t1.dummy()
# t2 = Test(97, 100)

# t1.info()
# t1.info()
# t2.info()

# Test.info()
# Test.info2()

# print(len('test'))
# print(sum([1,2,3,4,-1]))