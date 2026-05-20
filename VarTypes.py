# # instance Variable

# class New:
#     def __init__(self):
#         self.a = 10


# obj1 = New()
# obj2 = New()
# obj3 = New()
# obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


# Static Variable
class New:
    a = 10

    def __init__(self):
        self.name = "prashant"


obj1 = New()
obj2 = New()
obj3 = New()
New.a = 50
print(obj1.a)
print(obj2.a)
print(obj3.a)


class College:
    clgName = "modern College"  # static

    def __init__(self):
        self.stdName = "Aarya"  # instance


principal = College()
teacher = College()
accountant = College()
print("principal = ", principal.clgName, "------------", principal.stdName)
print("teacher = ", teacher.clgName, "------------", teacher.stdName)
print("accountant = ", accountant.clgName, "------------", accountant.stdName)

College.clgName = "RBU"  # second way to add static var
principal.stdName = "Aarya Saraf"
print("principal = ", principal.clgName, " | ", principal.stdName)
print("teacher = ", teacher.clgName, " | ", teacher.stdName)
print("accountant = ", accountant.clgName, " | ", accountant.stdName)
