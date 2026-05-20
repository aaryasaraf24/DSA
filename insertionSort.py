# insertion sort the comaparsion starts from 2nd[key] element and checks the 1st element if it is larger then swap
# likewise incement the key and keep checking all the elements that are before the Keyboard


arr = [5, 3, 6, 8, 2]
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while (j >= 0 and arr[j] > key):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = key
print(arr)
