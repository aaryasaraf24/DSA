def findbiggestnumber(samplearray):
    biggestnumber = samplearray[0]
    for index in range(1, len(samplearray)):
        if samplearray[index] > biggestnumber:
            biggestnumber = samplearray[index]
    print(biggestnumber)


samplearray = [5, 7, 9, 2, 3, 4]
findbiggestnumber(samplearray)

# time complexity ==> O(N) where N is the number of elements in the array
