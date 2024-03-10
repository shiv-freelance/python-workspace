# abstraction:
# hiding the implementation from the end-user

# 1. hiding -> doesn't expose the data
# 2. with abstraction, we can enforce if you want to inherit

# i. a abstract class can have both implementation methods and asbtract methods.
# ii. once a abstract class created, you can't create a object of it.

from abc import ABC, abstractmethod


class ReserveBank(ABC):  # abstract Base class

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    def test(self):
        print("i am a test method")


class ShivBank(ReserveBank):
    def deposit(self):
        print("i collect the money!!!")

    def withdraw(self):
        print("customer can withdraw now!!!")


bank = ShivBank()
bank.deposit()
bank.withdraw()
bank.test()
