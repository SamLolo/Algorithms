
# Mixed array of integers & get integer to find index of from user
ToSearch = [1, 4, 7, 2, 8, 6, 9, 3, 10, 5]
ToFind = int(input())

# Iterate through the array until the value is found
for i in range(len(ToSearch)):
    if ToSearch[i] == ToFind:
        print(str(i+1)+"th Position")
        break
