

print("Hello World!!!") # output statement

name = input("please enter your name") # input statement

# this is print function, which prints the data into console.
print(name, type(name)) # using type function, you can find the datatype of a variable.

name = int(name) # type conversion
print(name, type(name))

# string declaration
test: str = "test" 
print(test)


# to get a list of keywords.
import keyword
print(keyword.kwlist)



['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']



# boolean: True, False
# Undefined: None
# condition: and, or, if, elif, else
# method: def, pass, return, async
# loop: for, while, with, continuem break
# exception: try, except, else, finally, raise
# import: from, import
# membership: in, not, in
# identity: is, is not
# aliasing: as
# anynomous: lambda
# delete: del
# variable: global, nonlocal



# int variable (Whole number)
age:int = 23
print(age)


# floating value (decimal value)
salary: float = 2343.45
print(salary, type(salary))


# String
string = 'Akshara'
print(string, type(string))
print(string.upper())


# Conditional statements
name = "Subhash"
age = 26 if name == "Subhsh" else 40, 'test', 'test2'

print(age, type(age))



############ sample program ###############

name: str = input('please enter your name: ')
age: str = input(f'{name} enter your age: ')

age: int = int(age)

if age >= 18:
    print('you are eligible for vote')
else:
    print('not eligible please come once you are 18')

