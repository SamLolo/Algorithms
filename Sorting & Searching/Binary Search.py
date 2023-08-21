array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = int(input())

midPointer = (len(array)-1) // 2
minPointer = 0
maxPointer = len(array)-1

while minPointer != maxPointer:
    if toFind < array[midPointer]:
        maxPointer = midPointer
        midPointer //= 2
    elif toFind > array[midPointer]:
        minPointer = midPointer
        midPointer = minPointer + ((maxPointer - minPointer) // 2)
    else:
        minPointer = maxPointer = midPointer
        
    print(minPointer, maxPointer)   
print(minPointer)
