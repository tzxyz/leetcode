class MinStack:
    """
    设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
        push(x) -- 将元素 x 推入栈中。
        pop() -- 删除栈顶的元素。
        top() -- 获取栈顶元素。
        getMin() -- 检索栈中的最小元素。

    示例:
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin();   --> 返回 -3.
        minStack.pop();
        minStack.top();      --> 返回 0.
        minStack.getMin();   --> 返回 -2.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = None

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.min is None or self.min > x:
            self.min = x

    def pop(self) -> None:
        tail = self.data[-1]
        self.data = self.data[:-1]
        if tail == self.min:
            if self.data:
                self.min = min(self.data)
            else:
                self.min = None

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min


if __name__ == '__main__':
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.pop()
    print(s.getMin())