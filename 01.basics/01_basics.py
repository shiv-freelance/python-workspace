print("Hello World!!!")  # output statement

name = input("please enter your name")  # input statement

# print function, which prints the data into console or terminal.
print(name, type(name))  # using type function, you can find the datatype of a variable.


# to get a list of keywords.
import keyword

print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# boolean: True, False
# Undefined: None
# condition: and, or, if, elif, else
# method/function: def, pass, return
# loop: for, while, with, continuem break
# exception: try, except, else, finally, raise
# import: from, import
# membership: in, not, in
# identity: is, is not
# aliasing: as
# anynomous: lambda
# delete: del
# variable: global, nonlocal
# asynchronous: async, await
# class: class


# int variable (Whole number)
age: int = 23
print(age)


# floating value (decimal value)
salary: float = 2343.45
print(salary, type(salary))


# String
string = "Hari Ram"
print(string, type(string))

