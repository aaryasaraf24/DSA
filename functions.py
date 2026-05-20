# function vs method
# method is inside class called using dot operator
# function is outside class called using function name

# def arithematic():
#     a = int(input("Enter a value:"))
#     b = int(input("Enter b value:"))
#     sum = a+b
#     sub = a-b
#     mul = a*b
#     return sum, sub, mul

# when returning multiple values is returned in tuple because the values dont change in runtime

# print(arithematic())
# res = arithematic()
# print(res)

# positional arguments
# def arithematic(a, b):
#     a = int(input("Enter a value:"))
#     b = int(input("Enter b value:"))
#     sum = a+b
#     sub = a-b
#     mul = a*b
#     return sum, sub, mul


# res = arithematic(5, 5)
# print(res)

# keyword arguments
# parameter name and keyword name must be same
# def credential(username, pwd):
#     if username == pwd:
#         print("success")
#     else:
#         print("invalid")


# credential(pwd="admin", username="admin")


# default arguments
# def cityName(city="chennai"):
#     print(city)
# cityName("Nagpur")
# cityName()


# * selects all the arguments and stores in a tuple

# def cityName(*name):
#     print(name)

# cityName("Nagpur", "goa", "chennai", "pune")

import sys


def add():
    a = int(input("Enter a value:"))
    b = int(input("Enter b value:"))
    print(a+b)


def sub():
    a = int(input("Enter a value:"))
    b = int(input("Enter b value:"))
    print(a-b)


def mul():
    a = int(input("Enter a value:"))
    b = int(input("Enter b value:"))
    print(a*b)


def div():
    a = int(input("Enter a value:"))
    b = int(input("Enter b value:"))
    print(a/b)


while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        sys.exit()
