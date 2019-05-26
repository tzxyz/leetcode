class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        result = []
        if not self.data:
            return None
        while len(self.data) > 1:
            result.append(self.data.pop(0))
        x = self.data.pop(0)
        self.data = result
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        result = []
        if not self.data:
            return None
        while len(self.data) != 1:
            result.append(self.data.pop(0))
        x = self.data.pop(0)
        result.append(x)
        self.data = result
        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.data


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
