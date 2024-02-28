# Inheritance:
    #  if I inherit a super class from a child class all the properites and methods of a super class I can access it from child.

# super class
class Tree:
    is_flower = True # public variable.

    def give_fruit(self):
        print("here is the fruit")

    def give_oxygen(self):
        print('Oxygen is released!!')


# child class
class Apple(Tree): # Apple extends Tree >>> Java
    def test(self):
        print('test function')


apple1 = Apple() # Apple 

apple1.give_fruit()
apple1.give_oxygen()
print(apple1.is_flower)
apple1.test()

tree = Tree()
tree.is_flower
tree.give_fruit()
tree.give_oxygen()

tree.test()

#####################################################################3

class Father:
    def test_father(self):
        print('father method')
    
    def smoking(self, flag: bool):
        if flag:
            print('son is smoking')
        else:
            print('He is a good boy!!!')

class Son(Father):
    pass

son = Son() # child object
son.test_father()
son.smoking(False)

# father = Father()
# father.smoking()


#############################################


class Father:
    def move(self):
        print('I can Walk!!!')


class Son(Father):
    # method overriding: if a method from super class declared the same method signature in child class is called overriding.
    def move(self):
        # super().move() # to call the super class method.
        print('I can run as well!!!')

    def trekking(self):
         print('I can do trekking')


son = Son()
son.move()
# son.trekking()

# father = Father()
# father.move()


########################### Assignement ###########################

# super class: Animal - make_sound
# child class: Dog - make_sound

# dog = Dog(); dog.make_sound()


class Animal:

    def walk(self, legs):
        return legs
    
    def test(self):
        print('test method')
    
class Elephant(Animal):
    def walk(self):
        print(super().walk(4)) # 4
        super().test()
        print("can't walk anymore!")


e = Elephant()
# print()
e.walk()

# A, B, C - SUBCLASS

# single level, multi-level, hierachial, multiple 

########################################################################

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Employee(Person):
    pass

emp = Employee()


#########################################################33

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self) -> None:
        super().__init__('Ganesh', 26)
        print('employee constructor called!')


print(Employee.__mro__)


