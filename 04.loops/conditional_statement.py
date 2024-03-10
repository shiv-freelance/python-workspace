name: str = input("please enter your name: ")
age: str = input(f"{name} enter your age: ")

age: int = int(age)

if age >= 18:
    print("you are eligible for vote")
else:
    print("not eligible please come once you are 18")
