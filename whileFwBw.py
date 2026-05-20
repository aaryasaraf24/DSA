# s = "Learning Python is very easy"
# n = len(s)
# i = 0
# print("Forward Direction")
# while i < n:
#     print(s[i], end=' ')
#     i += 1
# print("\n")
# print("Backward Direction")
# i = -1
# while i >= -n:
#     print(s[i], end=' ')
#     i = i-1


# Check the sent and received data are same or not and find the missing string

# strSent = input("enter the string sent : ")
# strReceived = input("enter the string received : ")
# if (strSent == strReceived):
#     print("data received successfully")
# else:
#     for i in strSent:
#         if i not in strReceived:
#             print("missing string is ", i)


# find vowels in a given string (unique)
# vowels = ['a', 'e', 'i', 'o', 'u']
# found = []
# word = input("enter a word")
# for i in word:
#     if i in vowels:
#         if i not in found:
#             found.append(i)
# print("vowels in the word are ", found)


# import datetime

# date = datetime.datetime.now()
# print("now:{:%d-%m-%Y %H:%M:%S}".format(date))


# x = ['A', 'B', 'C', 'D']
# y = ['A', 'B', 'C', 'D']
# z = [1, 2, 3, 4]
# print(x == y)
# print(x == z)
# print(x != z)
# #o/p
# True
# False
# True

# squares = {x: x*x for x in range(1, 6)}
# print(squares)

# doubles = {x: 2*x for x in range(1, 6)}
# print(doubles)

# username="admin"
# pwd="admin"


# while True:
#     username = input("enter username: ")
#     pwd = input("enter Password : ")
#     if (username == 'admin' and pwd == 'admin'):  # if username == pwd:
#         print("login")
#         break
#     else:
#         print("Try Again")
