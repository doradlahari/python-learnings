# Exception : Error

# Exception Handlings : handlings the errors...

list1=[21,5.6,'python',43,0,12]

# for ele in list1:
#     print(1/ele)

# 2 types of exception:
    # in built
    # userdefined exceptions

# syntax

"""
try:
    statements(those lines of code which might give error)
except:
    statements(those lines which i have to exceute when ever an error is occuered...)
"""


# for ele in list1:
#     try:
#         print(1/ele)
#     except:
#         print("Error Occured")

# import sys
# 
# for ele in list1:
    # try:
        # print(1/ele)
        # sys.data
    # except TypeError:
        # print(sys.exc_info()[0])
        # print('invalid type of data, please provide correct type of fata')
    # except ZeroDivisionError:
        # print('You can not divide by zero')
    # except:
        # print('Some other error has occurred')

# userdefined exceptions

# class ValueSmallError(Exception):
#     pass

# class ValueLargeError(Exception):
#     pass
# import random
# num1=random.randint(100,500)

# while True:
#     num2= int(input('enter your number:'))
#     try:
#         if num2>num1:
#             raise ValueLargeError("Your value is too large")
#         elif num2<num1:
#             raise ValueSmallError("your value is too small")
#         else:
#             print('number guessed')
#     except ValueSmallError:
#         print('value entered is smaller, try with larger value.')
#     except ValueLargeError:
#         print('value entered is larger, try with smaller2 value.')


