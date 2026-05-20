# mydict = {
#     101: "python",
#     102: "java",
#     "103": "c++",
#     104: "javascript",
#     105: "python",
#     101: "java",
#     103: "c"

# }
# print(mydict)
# a = mydict[101]
# print(a)

# mydict[101] = "ruby"
# print(mydict)

# for x in mydict:
#     print(x)  # will print keys

# print("-----------------")
# for x in mydict.values():
#     print(x)  # will print values


# print("-----------------")
# for x in mydict.items():
#     print(x)  # will print key value pair as tuple


# mydict.pop(101)
# print(mydict)

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# box = {}
# jars = {}
# crates = {}
# box['b'] = 1
# box['c'] = 3
# jars['jams'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

# dict = {'c': 97, 'a': 96, 'bb': 98}
# for _ in sorted(dict):
#     print(dict[_])

# max value in a dictionary
# dict = {'c': 97, 'a': 96, 'bb': 98}
# max = max(dict.keys())
# print(max)
# min = min(dict.keys())
# print(min)

# count the frequency of elements
dict = [1, 2, 3, 4, 5, 6, 2]
print(dict.count(2))
print(dict.count(1))
print(dict.count(3))
print(dict.count(5))
print(dict.count(4))
