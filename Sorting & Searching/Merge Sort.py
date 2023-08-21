import math

ToSort = [[1, 4,10, 7, 11, 2, 8, 12, 6, 13, 3, 5, 9]]
ArrayNum = len(ToSort[0])
    
while len(ToSort) < ArrayNum:
    for i in range(len(ToSort)):
        if len(ToSort[i]) > 1:
            Array = ToSort.pop(i)
            ToSort.insert(i, Array[(len(Array) // 2):])
            ToSort.insert(i, Array[:(len(Array) // 2)])

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
        
print(ToSort[0])