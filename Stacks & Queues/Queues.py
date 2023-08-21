
class Queue():
    
    def __init__(self):
        
        self.array = [None, None, None, None, None, None, None, None, None, None]
        self.inpointer = 0
        self.outpointer = 0
        self.maxsize = 9
        
    def check_empty(self):
        
        if self.array[self.outpointer] != None:     
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
        
        if self.check_empty():
            
            Data = self.array[self.outpointer]
            if self.outpointer == self.maxsize:
                self.outpointer = 0
            else:
                self.outpointer += 1
                
            return Data
                
        else:
            print("Nothing To Dequeue!")
            return None
            
            
Queue = Queue()

Data = Queue.dequeue()
print(Data)
    
Queue.enqueue("Sam")

Data = Queue.dequeue()
print(Data)

        
    
    