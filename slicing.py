# name = "prashantjha"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[15]) #outofbound
# print(name[0:5])
# print(name[:5]) #start to 4
# print(name[0:]) #to last
# print(name[0:5:2]) #jump 2

# s = "Python is high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title()) #1st letter of all words
# print(s.capitalize()) #only 1st char


# formatting output
# age = 22
# print("age is {}".format(age))
# A = 1
# print(f"{A} is a good number")


# string functions
# true if all char are either alphabets or numbers
# print('aaryasaraf24'.isalnum())
# print('aaryasaraf'.isalpha())  # true if all char are alphabets
# print('1234ff'.isdigit())  # true if all char are digits
# print('Aarya'.islower())  # true if all char are lowercase
# print('AARYA'.isupper())  # true if all char are uppercase
# print(' '.islower())  # false because space is not a lowercase character
# print(' '.isspace())  # true because space is a whitespace character
# # true because each word starts with an uppercase letter
# print('My Name Is aarya'.istitle())
# print("Hello".startswith("h"))  # true because string starts with "H"
# print("Hello".endswith("le"))  # true because string ends with "o"


# returns -1 because "z" is not found in the string
print("Prashant".find("z"))
print("Prashant".find("a"))  # returns 2 because "a" is found at index 2
print("prashant".index("h"))  # returns 4 because "h" is found at index 4
# returns 2 because "a" is found twice in the string
print("prashant".count("a"))
