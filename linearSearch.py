def linearSearch(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return i
    return -1


array = [1, 2, 3, 4, 7, 9]
target = 7
result = linearSearch(array, target)
if result == -1:
    print("not found")
else:
    print("found at index", result)
