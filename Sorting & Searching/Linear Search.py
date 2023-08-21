
ToSearch = [1, 4, 7, 2, 8, 6, 9, 3, 10, 5]

ToFind = int(input())
for i in range(len(ToSearch)):
    if ToSearch[i] == ToFind:
        print(str(i+1)+"th Position")
