ToSort = [1, 4, 7, 2, 8, 6, 9, 3, 10, 5]

for i in range(len(ToSort)):
    for i in range(len(ToSort)-1):
        if ToSort[i] > ToSort[i+1]:
            Temp = ToSort.pop(i)
            ToSort.insert(i+1, Temp)
            
print(ToSort)