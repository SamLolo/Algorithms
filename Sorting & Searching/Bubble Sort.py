
# Mixed array of integer values from 1 to 10 to sort
ToSort = [1, 4, 7, 2, 8, 6, 9, 3, 10, 5]

# Iterate through the array n times (where n is the length of the array)
for i in range(len(ToSort)):
    for i in range(len(ToSort)-1):
        
        # For each value, compare it to the next value and if it's bigger, swap the two values
        if ToSort[i] > ToSort[i+1]:
            Temp = ToSort.pop(i)
            ToSort.insert(i+1, Temp)

# Print out resulting sorted array        
print(ToSort)