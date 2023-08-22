
# Presorted array of integers & get integer to find from user
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = int(input())

# Set the midpoint at the middle of the array (choosing the left value if middle is between 2 values)
# Set the minpoint at 0 and the maxpoint at the end of the array
midPointer = (len(array)-1) // 2
minPointer = 0
maxPointer = len(array)-1

# While minpointer and maxpointer don't match, compare value to find to value at midpoint
# If value is lower, set max pointer at previous midpoint and find new midpoint of remaining array
# If value is higher, set min pointer at midpoint
while minPointer != maxPointer:
    if toFind < array[midPointer]:
        maxPointer = midPointer
        midPointer //= 2
    elif toFind > array[midPointer]:
        minPointer = midPointer
        midPointer = minPointer + ((maxPointer - minPointer) // 2)
        
    # If value matches midpoint, you've found the correct position in the array
    else:
        minPointer = maxPointer = midPointer
    
    # Print progress of binary search and output min point as index of the value being searched
    print(minPointer, maxPointer)   
print(minPointer)
