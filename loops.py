# name = "Aarya"
# for i in name:
#     print(i)

# wap to remove duplicate characters from a string
# i/p -- aarya
# o/p -- ary
name = "aarya"
newname = ""

# for i in name:
#     if i not in newname:
#         newname += i //newname=newname+i
# print(newname)
# will not have duplicate
# N = len(name)
# for i in range(N-1, -1, -1):
#     # write name[i] in reverse order because we are iterating from last to first we cannot directly concatnet
#     newname += name[i]
# print(newname)

# has duplicate
# name = "aarya"
# reversename = ""
# for i in name:
#     reversename = i+reversename
# print(reversename)


# different wasy to reverse a string
# name="prashant"
# #1 using slicing [::-1]
# reversed_name = name[::-1]
# print(reversed_name)
# #2 using reversed() function
# reversed_name = ''.join(reversed(name))
# print(reversed_name)
# #3 using a loop
# reversed_name = ""
# for char in name:
#     reversed_name = char + reversed_name
# print(reversed_name)
