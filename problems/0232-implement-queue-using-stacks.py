class MyQueue:
    """
    使用栈实现队列的下列操作：

        push(x) -- 将一个元素放入队列的尾部。
        pop() -- 从队列首部移除元素。
        peek() -- 返回队列首部的元素。
        empty() -- 返回队列是否为空。

    示例:

        MyQueue queue = new MyQueue();
        queue.push(1);
        queue.push(2);
        queue.peek();  // 返回 1
        queue.pop();   // 返回 1
        queue.empty(); // 返回 false

    说明:

        你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
        你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
        假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.data:
            s = []
            while len(self.data) > 1:
                s.append(self.data.pop(-1))
            x = self.data.pop(-1)
            while s:
                self.data.append(s.pop(-1))
            return x

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.data:
            s = []
            while len(self.data) > 1:
                s.append(self.data.pop(-1))
            x = self.data[-1]
            while s:
                self.data.append(s.pop(-1))
            return x

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.data


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.empty() is True
