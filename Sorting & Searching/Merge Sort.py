import math

# Given a 2D array of numbers to sort, get the length of the inner array
ToSort = [[1, 4, 10, 7, 11, 2, 8, 12, 6, 13, 3, 5, 9]]
ArrayNum = len(ToSort[0])

# Keep splitting the inner arrays into 2 arrays equal in size (+/-1) until ToSort is an array of arrays of length 1
while len(ToSort) < ArrayNum:
    for i in range(len(ToSort)):
        if len(ToSort[i]) > 1:
            Array = ToSort.pop(i)
            ToSort.insert(i, Array[(len(Array) // 2):])
            ToSort.insert(i, Array[:(len(Array) // 2)])

# While the array is still split, join each pair of lists together with each other, comparing each value in the right array
# with those inside the left array and ordering them as they're merged back together
while len(ToSort) > 1:
    for i in range(math.ceil(len(ToSort) / 2)):
        if i+1 < len(ToSort):
            for Value in ToSort[i+1]:
                for j in range(len(ToSort[i])):
                    if ToSort[i][j] > Value:
                        ToSort[i].insert(j, Value)
                        break
                if not(Value in ToSort[i]):
                    ToSort[i].append(Value)
            ToSort.pop(i+1)

# Print out the final sorted inner array    
print(ToSort[0])