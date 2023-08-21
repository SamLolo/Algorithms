
#!---------------------------Graphs----------------------------#

graph = {'A':['B', 'C'],
         'B': ['A', 'F'],
         'C': ['A', 'D', 'E'],
         'D': ['C', 'H', 'J'],
         'E': ['C', 'F', 'J'],
         'F': ['B', 'G'],
         'G': ['F', 'H'],
         'H': ['D', 'G', 'I'],
         'I': ['H', 'K'],
         'J': ['D', 'E', 'K', 'M'],
         'K': ['I', 'J'],
         'M': ['J']}

graph2 = {'A':['B', 'C'],
          'B': ['A', 'D', 'E'],
          'C':['A', 'E'],
          'D':['B', 'G'],
          'E':['B', 'C', 'F'],
          'F':['E'],
          'G': ['D']}


#!---------------------------Stacks & Queues---------------------------!#


class Stack():
    
    def __init__(self):
        
        self.array = []
        self.pointer = -1
        self.maxsize = 10

    def push(self, data):
    
        if self.pointer < self.maxsize:
            self.pointer += 1
            self.array.append(data)
        else:
            print("Data Not Saved - Stack Full!")
            
    def pop(self):
        
        if self.pointer >= 0:
            data = self.array.pop(self.pointer)
            self.pointer -= 1
            return data
        else:
            print("There is no data to pop from stack")
            
    def peep(self):
        
        if self.pointer >= 0:
            data = self.array[self.pointer]
            return data
        else:     
            print("There is no data to peep at!")
            
            
class Queue():
    
    def __init__(self):
        
        self.array = [None, None, None, None, None, None, None, None, None, None]
        self.inpointer = 0
        self.outpointer = 0
        self.maxsize = 9
        
    def check_empty(self):
        
        if self.inpointer == self.outpointer and self.array[self.outpointer] != None:     
            return True
            
        return False
        
    def check_full(self):
        
        if self.inpointer == self.outpointer and self.array[0] != None:
            return True
        
        return False
        
    def enqueue(self, data):
        
        if not(self.check_full()):
            
            self.array[self.inpointer] = data
            if self.inpointer == self.maxsize:
                self.inpointer = 0
            else:
                self.inpointer += 1
                
            print(self.array)
            
        else:
            print("Queue is full!")
            
        
    def dequeue(self):
        
        if not(self.check_empty()):
            
            Data = self.array[self.outpointer]
            if self.outpointer == self.maxsize:
                self.outpointer = 0
            else:
                self.outpointer += 1
                
            return Data
                
        else:
            print("Nothing To Dequeue!")
            return None
             

#!----------------------Traversal Methods-----------------------!#


class DepthTraversal(Stack):
    
    def __init__(self, Graph):
        
        super().__init__()
        self.Graph = Graph
        self.Visited = []
        self.Path = []
    
    def check_visited(self, Node):
        
        for NewNode in self.Graph[Node]:
            
            if not(NewNode in self.Visited):
                return False, NewNode
            
        return True, None
    
    def check_completed(self):
        
        for Key in self.Graph.keys():
            
            if not(Key in self.Visited):
                return False
            
        return True
    
    def start(self):
        
        self.push('A')
        self.Visited.append('A')
        self.Path.append('A')
        
        while self.array != []:
            
            Node = self.peep()
            Completed, NewNode = self.check_visited(Node)
            if not(Completed):
                
                self.push(NewNode)
                self.Visited.append(NewNode)
                self.Path.append(NewNode)
            
            else:
                
                self.pop()
                LastNode = self.peep()
                Completed, NewNode = self.check_visited(Node)
                AllVisited = self.check_completed()
                if LastNode != None and (not(Completed) or not(AllVisited)):
                    self.Path.append(LastNode)
                
        print(self.Path)
        return "".join(self.Path)


class BreadthTraversal(Queue):
    
    def __init__(self, graph):
        
        super().__init__()
        
        self.Graph = graph
        self.Visited = []
        self.Path = []

    def check_visited(self, Node):
        
        if Node in self.Visited:
            return True
            
        return False

    def start(self):
        
        self.enqueue('A')
        self.Visited.append('A')
        NextNode = 'A'
        
        while not(self.check_empty()) and NextNode is not None:
            
            for Node in self.Graph[NextNode]:
                
                if not(self.check_visited(Node)):
                    self.enqueue(Node)
                    self.Visited.append(Node)
            
            NextNode = self.dequeue()
            if NextNode is not None:
                self.Path.append(NextNode)
            
        print(self.Path)
        return "".join(self.Path)


#!-----------------------Main Function----------------------------!#

    
def main():
    
    Method = input("Select Traversal Method: ")
    if Method.lower() == "depth":
        
        Depth = DepthTraversal(graph)
        Path = Depth.start()
        print(Path)
        
    elif Method.lower() == "breadth":
        
        Breadth = BreadthTraversal(graph)
        Path = Breadth.start()
        print(Path)
        
    else:
        print("Method Doesn't Exist!")
            

if __name__ == "__main__":
    main()