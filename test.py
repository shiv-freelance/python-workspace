class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg


voters = []  # global variable


class Voter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(
        self,
    ):  # string magic method --> this will give string representation of your object
        return f"Name of the voter is: {self.name} and age is {self.age} registered"


def register_voter(name, age):
    try:
        if age < 18:
            raise TooYoungException("too young to cast a vote")
        v = Voter(name, age)
        voter_details = {"name": v.name, "age": v.age}
        voters.append(voter_details)
        return v
    except Exception as exec:
        print(exec)


def menu():
    print(
        """
    Welcome to Voter registration Portal:
          press:
            1. for voter registeration
            2. to cast a vote.

"""
    )
    choice = input("enter your choice: ")

    if choice == "1":
        print('enter the details for registration')
        name = input('please enter your name: ')
        age = int(input('enter your age: '))
        v = register_voter(name, age)

    print(voters)


menu()