class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.shell = []

    def push(self, x: int) -> None:
        self.shell.append(x)
        
    def pop(self) -> None:
        if self.shell!=[]:
            self.shell = self.shell[:-1]
        
    def top(self) -> int:
        if self.shell!=[]:
            return self.shell[-1]

    def getMin(self) -> int:
        if self.shell!=[]:
            return min(self.shell)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()