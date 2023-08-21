
import operator

class stack():
    
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
            
            
def main():
    
    RPN = input("Please enter the Reverse Polish Notation: ")
    
    RPN = RPN.split(" ")
    print(RPN)
    Stack = stack()
    
    for Value in RPN:
        
        if Value.isdecimal():
            
            Stack.push(Value)
            
        else:
            
            Value2 = int(Stack.pop())
            Value1 = int(Stack.pop())
            
            Operands = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "%": operator.mod, "^": operator.xor}
            NewValue = Operands[Value](Value1, Value2)
            
            Stack.push(NewValue)
            
    print(Stack.peep())
    
    
if __name__ == "__main__":
    main()    