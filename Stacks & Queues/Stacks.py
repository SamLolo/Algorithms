
class stack():
    
    def __init__(self):
        
        self.array = ["Sam", None, None, None, None, None, None, None, None, None]
        self.pointer = 0

    def push(self, data):
    
        if self.pointer < len(self.array):
            
            self.pointer += 1
            self.array[self.pointer] = data
            
        else:
            print("Data Not Saved - Stack Full!")
            
    def pop(self):
        
        if self.pointer > 0:
            
            data = self.array[self.pointer]
            self.pointer -= 1
            
            return data
        
        else:
            print("There is no data to pop from stack")
            
    def peep(self):
        
        if self.pointer > 0:
            
            data = self.array[self.pointer]
            
            return data
        
        else:
            
            print("There is no data to peep at!")
        

Stack = stack()
Stack.push("Dom")
print(Stack.array)

Data = Stack.pop()
print(Data)

Data = Stack.peep()
print(Data)