
class Stack:
    def __init__(self): # stack() constructor
        self._index = []

    def push(self, item): # adds an item to top of stack
        self._index.append(item)

    def peek(self): # returns the top item of stack without removing it
       if not self._index:
           raise IndexError("peek from empty stack")
       return self._index[-1]

    def pop(self): # removes and returns the top item of stack
       if not self._index:
           raise IndexError("pop from empty stack")
       return self._index.pop()

    def is_empty(self): # returns True if stack is empty, False otherwise
       return len(self._index) == 0
    def size(self): # returns the number of items in the stack
        return len(self._index)


    
