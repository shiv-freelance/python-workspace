

# print "hello world"

# 1. SyntaxError
    # print "hello world"

# if True:
#     print('hello')
# iwoigj = 1
#     ejroijo = 0

# 2. RuntimeError

# try: 
#     pass
#     # exception code
# except:
#     pass
#     # handled the errored handling.

# # try:
# #     100/2
# # except:
# #     print('dude, you are divison with zero')
# # finally:
# #     # no matter what, this block of code will be executed.
# #     print("finally block")
# # # 100/0

# # print('after handled code.')

# # this block of code, will stop the exection of finally block by shutting down the PVM.
# # import os
# # try:
# #     100/0
# # except:
# #     print('dude, you are divison with zero')
# #     os._exit(0)
# # finally:
# #     # no matter what, this block of code will be executed.
# #     print("finally block")

# # not possible
# # try:
# #     pass
# # finally:
# #     pass
# # except:
# #     pass

# # this works
# # try:
# #     100/2
# # finally:
# #     print('finally')

# # try:
# #     pass
# # except:
# #     pass

# # except:
# #     pass


# def division(a:str, b:str) -> float:
#     try:
#         a = int(a)
#         b = int(b)
#         return a/b
#     # except ZeroDivisionError:
#     #     print(f'exception has raised while division of {a}, {b}')
#     # except ValueError:
#     #     print('while converting(str to int) got value error')
#     except (ZeroDivisionError, ValueError) as msg:
#         print(msg)


# a = input('first value: ')
# b = input('second value: ')

# div = division(a,b)
# print(div)
# System.out.println('hello')

# raise >>> when ever you want raise an exception.


# def div(a, b):
#     # if b == 0:
#     #     raise ZeroDivisionError("division with zero, will result error!")
#     a/b
# div(10, 0)

# person: name, age, gender

# if (age > 18 and gender == 'girl') or (gender =='male' or age > 21):
#     print('not eligable')
#     print('noierogijo')
#     print('3rd statement ')
# elif age < 50:
#     print("over aged, your time is gone! to get married")

class TooYoungException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg
class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg

# age validation
def age_validation(age: int):
    try:
        if age < 21:
            raise TooYoungException("Dude!, please wait some time unitl you cross 21")
        elif age > 40 and age <= 60:
            raise TooOldException("Grandpa! your turn is over")
        elif age > 60:
            raise TooOldException("you are above 60, take care of grand children")
        else:
            print('okay!, you can register with us')
    except (TooYoungException, TooOldException) as msg:
        # handling the exception
        print('we got exception', msg)
    except Exception:
        print('got type error, str comparision with int')
    except:
        print('test')
    else:
        print('will get execute, only if there in no excepiton in try block')
    finally:
        print("I will get execute man, no matter what (exception raised or not)")

name = "Shiv"
age = 27
gender = 'Male'

age_validation(age)



# dict

# d1 = {"name": "shiv", "age": 27, "mail": "username@gmail.com"}
# print(d1.get('nmae', "Perter Parker"))