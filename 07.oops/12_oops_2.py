# variables.

# global variables
# local variables.

name = "Shiv"  # global


def test():
    # name = "Raj"
    print(name)


def test1():
    name = "Krishna"
    global age
    age = 27
    print(name)


test()  # shiv
# test1() # krishna
print(age)


# name = "Shiv" # global

# def test():
#     # name = "Raj"
#     print(name)
#     print(age)

# def test1():
#     name = "Krishna"
#     global age
#     age = 27
#     print(name)

# test1() # krishna
# test() # shiv

# print(age)


# access global variable

name = "Shiv"  # global


def test1():
    name = "Krishna"  # local
    print(name)
    print(globals()["name"])


test1()  # krishna

# calling one func from inside of a func
email = "user@gmail.com"


def func1():
    print(email)
    func2()
    func3()


def func2():
    print(email)


def func3():
    print(email)


func1()


# infinite loop
email = "user@gmail.com"


def func1():
    print(email)
    func2()


def func2():
    print(email)
    func3()
    func1()


def func3():
    print(email)


func1()
