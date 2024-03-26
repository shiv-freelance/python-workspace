
name = "shivFreeLancer"

# case change
print(name.upper()) # SHIVFREELANCER
print(name.lower()) # shivfreelancer
print(name.capitalize()) # Shivfreelancer

# boolean checks
print(name.isupper())
print(name.islower())
print(name.istitle())

# check characters
print(name.isalpha()) # True
print(name.isdigit()) # False (checks atleast one digit present or not)
print(name.isalnum()) # True
print(name.isnumeric()) # is entire string number or not.

# count
print(name.count('a')) # returns the no.of occurances of a string

# comparision
print(name.casefold()) #shivfreelancer

# finding
print(name.find('shiv')) # checks the substring (returns the index position).

# print(name.center(3)) # returns a centered string.

print(name.startswith('s')) # checks specific characters starts with?
print(name.endswith('k')) # False

print("9999".zfill(10)) # fills a string to match the length.
