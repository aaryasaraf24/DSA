
# if want to print same numbers or alphabets in a row then print i
# if one row contains differnet numbers or alphabets then print j


# for i in range(1, 4):  # rows
#     for j in range(1, 4):  # columns
#         print(i, end=" ")
#     print()

# print("----------------------------")
# for i in range(1, 4):  # rows
#     for j in range(1, 4):  # columns
#         print(j, end=" ")
#     print()


# chr function converts the ascii values into their corresponding characters
# print("----------------------------")
# n = int(input("enter the number of rows : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         # 64+1 because we want ascii value of capitaal A to be printed when i=1
#         print(chr(64+i), end=" ")
#     print()

# print("----------------------------")
# n = int(input("enter the number of rows : "))
# for i in range(1, n+1):
#     for j in range(1, 1+i):  # to print 1 char in 1st row, 2 char in 2nd row and so on
#         print("*", end=" ")
#     print()

# print("----------------------------")
# n = int(input("enter the number of rows : "))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):  # to print 1 char in 1st row, 2 char in 2nd row and so on
#         print(chr(64+i), end=" ")
#     print()


# import time
# n = int(input("enter the number of rows:"))
# for i in range(1, n+1):
#     print(" "*(n-i), end=" ")
#     for j in range(1, i+1):
#         time.sleep(2)
#         print("*", end=" ")
#     print()


# i/p=[1,2,3,4]
# o/p=[24,12,8,6]
