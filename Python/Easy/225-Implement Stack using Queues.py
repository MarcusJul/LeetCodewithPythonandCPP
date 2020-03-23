class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.s.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        ret = self.s[-1]
        self.s = self.s[:-1]
        return ret

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.s[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if self.s==[] else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()