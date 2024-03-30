# condition statement keywords: if, else, elif

# Syntax:
condition = True

if condition:
    print("this get's executed if condition satisfies(True)")
else:
    print("if condition fails then else block get's executed")


if condition:
    print('if block')
elif condition:
    print('elif block')
else:
    print('else block')


# Conditional statements
name = "Shiv"
age = 26 if name == "Shiv" else 40, "test", "test2"

print(age, type(age))


############ sample program ###############

name: str = input("please enter your name: ")
age: str = input(f"{name} enter your age: ")

age: int = int(age)

if age >= 18:
    print("you are eligible for vote")
else:
    print("not eligible please come once you are 18")