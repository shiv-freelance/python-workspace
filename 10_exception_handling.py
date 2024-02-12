

# print "hello world"

# 1. SyntaxError
    # print "hello world"

# if True:
#     print('hello')
# iwoigj = 1
#     ejroijo = 0

# 2. RuntimeError

try: 
    pass
    # exception code
except:
    pass
    # handled the errored handling.

# try:
#     100/2
# except:
#     print('dude, you are divison with zero')
# finally:
#     # no matter what, this block of code will be executed.
#     print("finally block")
# # 100/0

# print('after handled code.')

# this block of code, will stop the exection of finally block by shutting down the PVM.
# import os
# try:
#     100/0
# except:
#     print('dude, you are divison with zero')
#     os._exit(0)
# finally:
#     # no matter what, this block of code will be executed.
#     print("finally block")

# not possible
# try:
#     pass
# finally:
#     pass
# except:
#     pass

# this works
# try:
#     100/2
# finally:
#     print('finally')

# try:
#     pass
# except:
#     pass

# except:
#     pass


def division(a:str, b:str) -> float:
    try:
        a = int(a)
        b = int(b)
        return a/b
    # except ZeroDivisionError:
    #     print(f'exception has raised while division of {a}, {b}')
    # except ValueError:
    #     print('while converting(str to int) got value error')
    except (ZeroDivisionError, ValueError) as msg:
        print(msg)


a = input('first value: ')
b = input('second value: ')

div = division(a,b)
# print(div)
# System.out.println('hello')