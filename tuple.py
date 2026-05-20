# mytuple = ("prashant", "aarya", "aastha", 23, 65.10, "aarya")
# print(mytuple)
# print(type(mytuple))

# we cannot change the value of a tuple because it is immutable
# mytuple[2] = "priya"
# print(mytuple)

# init_tuple = ()
# print(init_tuple.__len__())  # 0

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a == init_tuple_b)  # True

# init_tuple_q = 1, 2
# init_tuple_w = (3, 4)
# print(init_tuple_q + init_tuple_w)  # (1, 2, 3, 4)

# l = [1, 2, 3,]
# init_tuple = tuple('pyhton',)*(l.__len__()-l[::-1][0])
# print(init_tuple)

init_tuple = ('python')*3
print(type(init_tuple))
