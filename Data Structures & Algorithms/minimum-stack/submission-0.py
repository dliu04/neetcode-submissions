class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Find the minimum of the value compared to the top of minStack
        # only if self.minStack is not empty. Else choose val
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
