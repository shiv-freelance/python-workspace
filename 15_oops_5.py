

class Bank:

    bank_name = "SBI"

    def set_balance(self, balance):
        if isinstance(balance, (int | float)):
            self.__balance = balance
        else:
            raise TypeError(f"instead of string got {type(balance)}")

    def get_balance(self):
        return self.__balance

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f"instead of string got {type(name)}")

    def get_name(self):
        return self.name
    
    def set_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            raise TypeError(f"instead of string got {type(age)}")
    
    def get_age(self):
        return self.age
    

account1 = Bank()
# account2 = Bank("Nagesh", 21, 5000)
# account3 = Bank('Saif', 12, 1000)

# account1.balance = 5000
account1.set_name('Nagesh')
account1.set_age(21)
account1.set_balance(5000)

print(account1.get_name(), account1.get_balance(), account1.get_age())

account1.set_balance(4600)

print(account1.get_name(), account1.get_balance(), account1.get_age())
# print(account2.name, account2.balance, account2.bank_name)
# print(account3.name, account3.balance, account3.bank_name)

# Encapuslation:
#               wrapping the data members along with it's setter and getter methods.
