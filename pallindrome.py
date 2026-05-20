# str = "racexar"
# print(str)
# rev_str = str[::-1]
# if str == rev_str:
#     print("palindrome")
# else:
#     print("not pallindrome")


# # anagram
# # if 1 word's letters are same as other word's letters then they are anagram
# w1 = "listen"
# w2 = "silent"
# if sorted(w1) == sorted(w2):
#     print("anagram")


# vowels and consonants
# vowels = ['a', 'e', 'i', 'o', 'u']
# name = "hello"
# cons = 0
# vow = 0
# for i in name:
#     if i in vowels:
#         vow += 1
#     else:
#         cons += 1
# print("vowels : ", vow)
# print("consonants : ", cons)

# count the words in the string
# sen = "This is a sentence"

# count = 0
# for i in sen:
#     if i == " ":
#         count += 1
# print(count+1)

# ord() function concerts the alphabets into their corresponding ascii values
ip = "gasgg54@#vscsdls"
count = 0
for i in ip:
    z = ord(i)
    if (z >= 48 and z <= 57) or (z >= 65 and z <= 90) or (z >= 97 and z <= 122) or (z >= 0 and z <= 9):
        continue
    else:
        count += 1
print(count)
