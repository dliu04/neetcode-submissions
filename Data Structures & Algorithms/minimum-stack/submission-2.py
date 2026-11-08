class MinStack:

    def __init__(self):
        self.stack = []
        # Initialize a minStack that functions alongside
        # the other stack. Keeps track of latest min value
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Append minimum value to minStack
        # If not self.minStack, use val instead
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
