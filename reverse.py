# num = 123
# a = num % 10
# num = num//10
# b = num % 10
# c = num//10
# rev = a*100+b*10+c*1
# print(rev)

# # 123456 -->654321
# num = 123456


# currency calculator
# amt = int(input("Enter the amount: "))
# print("100 notes:", amt//100)
# print("50 notes:", (amt % 100)//50)
# print("20 notes:", ((amt % 100) % 50)//20)
# print("10 notes:", (((amt % 100 % 50) % 20)//10))
# print("5 notes:", (((amt % 100 % 50) % 20) % 10) // 5)
# print("2 notes:", ((((amt % 100 % 50) % 20) % 10) % 5)//2)


# maximum consecutive ones in an array
arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]

max_count = 0
count = 0
for i in arr:
    if i == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print("Maximum consecutive ones:", max_count)

# count the no of substring 'ab' in a string
str = "abababab"
count = 0
for i in range
