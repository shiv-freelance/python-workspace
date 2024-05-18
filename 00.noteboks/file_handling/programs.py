def reverse_string(string: str) -> str:
    return string[::-1]


def is_palindrome(string: str) -> bool:  # function annotations.
    reverse_str = reverse_string(string)  # string reverse

    # if reverse_string == string:
    #     return True
    # else:
    #     return False

    return True if reverse_str == string else False


# print(is_palindrome("madam"))


class Student:

    def __init__(self, name, age, city) -> None:
        self.name = name
        self.age = age
        self.city = city



        
