import math

def Sort(List):
    ToSort = [List]
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
            
    return ToSort[0]


Graph = {'A':{'B': 30, 'C': 20},
         'B': {'A': 30, 'C': 20, 'E': 60},
         'C': {'A': 30, 'B': 20, 'D': 30},
         'D': {'C': 30, 'E': 30},
         'E': {'B': 60, 'D': 30}}

Dict = {'Visited': {}, 'Distance': {}, 'Previous': {}}
for Column in Dict.keys():
    for Vertex in Graph.keys():
        if Column == 'Visited':
            Dict[Column][Vertex] = False
        elif Column == 'Distance':
            Dict[Column][Vertex] = 100000
        else:
            Dict[Column][Vertex] = None
Dict['Visited']['A'] = 0

while False in list(Dict['Visited'].values()):
    Distances = Sort(list(Dict['Distance'].values()))
    for i in range(len(Distances)):
        Vertex = list(Dict['Distance'].keys())[list(Dict['Distance'].values()).index(Distances[i])]
        if Dict['Visited'][Vertex] == False:
            print(Vertex)
            break
