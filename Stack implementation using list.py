class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        #length of stack number of elements
        return len(self._data)

    def is_empty(self):
        #return true if stack is empty
        return len(self._data) == 0

    def push(self,e):
        # add element e to top of stack
        self._data.append(e)

    def pop(self):
        #remove element from top of stack
        if self.is_empty():
            raise IndexError( 'empty stack' )
        return self._data.pop()

    def top(self):
        #return top element but do not remove
        if self.is_empty():
            raise IndexError( 'none' )
        return self._data[-1]
    
Stack = ArrayStack()
Stack.push(9)
Stack.push(2)
Stack.top()

Stack = [8, 2]
Stack.sort()
temp = Stack[0]
print(temp)


    
