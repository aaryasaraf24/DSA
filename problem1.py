# wap to accept stud name and marks from keybpard and create a dictionary . Also display stud marks by taking studnet name

mydict = {}
n = int(input("enter number of students"))
for i in range(n):
    name = input("enter student name")
    marks = (int(input("enter marks ")))
    mydict[name] = marks
print(mydict)

while True:
    name = input("Enter student name to get marks")
    marks = mydict.get(name, -1)  # -1 is written as default if name not found
    if marks == -1:
        print("Student not found")
    else:
        print("Marks of", name, "are :", marks)
    option = input("do you want to find another studnet(Yes|No)")
    if option == "No":
        break
print("thanks for using application")
