
# Encapsulation:
#       The process of wrapping the data members/properties along with it's data handlers (setter/getter).

class Bank:

    bank_name = "SBI"

    def set_balance(self, balance):
        if isinstance(balance, (int | float)):
            self.__balance = balance
        else:
            raise TypeError(f"instead of int/float got {type(balance)}")

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
            raise TypeError(f"instead of int got {type(age)}")
    
    def get_age(self):
        return self.age
    
    def deposit(self, amount: float):
        if amount < 0:
            print('Stupid!!!')
            return
        new_balance = self.get_balance() + amount
        self.set_balance(new_balance)
        # print(self.__balance) # private variable.
        return f"Congratulations!!! {amount} has been deposited."
        

    def withdraw(self, amount: float):
        if self.get_balance() < amount:   # 6000 < 10000 
            raise Exception("Can't withdraw")
            # print('Canot withdraw')
            # return
        
        new_balace = self.get_balance() - amount # 6000 - 2000 , 4000
        self.set_balance(new_balace)

        return f"Amount {amount}, please pick your cash...!"
    
    def menu(self):
        while True:
            print("""
            Please chooose your option!
              1. Deposit
              2. Withdraw
              3. Check Balance
              4. Exit
         """)
            choice = int(input('enter your choice here: '))
            if choice == 1:
                amount = float(input('Enter the amount to be deposited!!'))
                print(self.deposit(amount=amount))
            elif choice == 2:
                amount = float(input('Enter the amount to be withdraw!!'))
                print(self.withdraw(amount=amount))
            elif choice == 3:
                print(self.get_balance())
            elif choice == 4:
                break

account1 = Bank() # object creation.

# account2 = Bank("Nagesh", 21, 5000)
# account3 = Bank('Saif', 12, 1000)

# account1.balance = 5000
account1.set_name('Nagesh')
account1.set_age(21)
account1.set_balance(5000)

print(account1.get_name(), account1.get_balance(), account1.get_age())

# account1.set_balance(4600)

# print(account1.get_name(), account1.get_balance(), account1.get_age())

account1.menu()


# print(account2.name, account2.balance, account2.bank_name)
# print(account3.name, account3.balance, account3.bank_name)

# Encapuslation:
#               wrapping the data members along with it's setter and getter methods.



# DRY - Don't repeat Yourself.
