class MinStack:

    def __init__(self):
        self.items = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.items.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.items.pop()
        self.minStack.pop()
   

    def top(self) -> int:
        if not self.is_empty():
            return self.items[-1]
        return None

    def getMin(self) -> int:
        return self.minStack[-1]

    def is_empty(self):
        return len(self.items) == 0    
    def size(self):
        return len(self.items)