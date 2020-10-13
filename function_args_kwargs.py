#Args / kwargs
#
# def add(*min):
#     # return min
#     total = 0
#     for i in min:
#         total = total + i
#     return total
#
# print(add())
# print(add(5))
#
# print(add(4,5))
# print(add(5,8,4,2,10,11))

#Kwargs :
#This is used to use the keyword argumemt , and the output will be in the dictionary format.
#we use ** in kwargs  to convert keyword arguments to dictionary.

# def validation(**kwargs):
#     print(kwargs)
#
# # validation(name='mintoo',age=32,city='Chandigarh')
# validation(name='mintoo')
#
# def validation(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# # validation(name='mintoo',age=32,city='Chandigarh')
# validation(4,10, name='mintoo', age=50, city='Chd')

# Example , excersie:

# name = input("Please enter the name: ")
# age = input("Please enter your age: ")
# mob = input("Please enter your Mobile number: ")
#
# def val_details(*args, **kwargs):
#     print(kwargs)
#     if not kwargs['n']:
#         print("you have not entered the name")
#     elif not kwargs['a']:
#         print("you have not entered the age")
#     elif not kwargs['m']:
#         print("you have not entered the Mobile number")
#     else:
#         print("validation is SUCCESSFULL")
#
# val_details(n=name, a=age, m=mob)

#Function as an object: First step to decorators.

def add(num1, num2):
    print(num1 + num2)

def sub(num1, num2):
    print(num1 - num2)

# funcs = [add, sub]
funcs = {'+': add, '-': sub}
num1 = input("Please enter the first number: ")
num2 = input("Please enter second number: ")
sign = input("Please enter the sign: ")

# if sign == '+':
#     funcs[0](int(num1), int(num2))
# elif sign == '-':
#     funcs[1](int(num1), int(num2))
# else:
#     print("Unknown sign...")

if sign in funcs:
    funcs[sign](int(num1), int(num2))
else:
    print("Unknown sign...")


# print(add)
# func = add
# print(func)
# add(2,6)
# func(3,8)









































