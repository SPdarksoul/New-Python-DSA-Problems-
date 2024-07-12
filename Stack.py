class Stack:
    def __init__(self):
        self.item =[]
    
    def empty(self):
      return self.item == []
    
    def push(self, item):
       return self.item.append(item)
    
    def pop(self):
        if not self.empty():
            return self.item.pop()  # Remove and return the top element from the stack
        else:
            raise IndexError("pop from empty stack")
        
    def  peek(self):
        if not self.empty():
            return self.item[-1]
        else: return None
    def size(self):
        return len(self.item)
    





if __name__ == "__main__":
       stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)



   # Print the stack size
print("Stack size:", stack.size())  # Output: Stack size: 3

    # Peek at the top element of the stack
print("Top element of the stack:", stack.peek())  # Output: Top element of the stack: 3

    # Pop elements from the stack
print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 2

    # Check if the stack is empty
print("Is the stack empty?", stack.empty())  # Output: Is the stack empty? False

    # Pop the remaining element from the stack
print("Popped element:", stack.pop())  # Output: Popped element: 1

    # Check if the stack is empty now
print("Is the stack empty now?", stack.empty())  # Output: Is the stack empty now? True
