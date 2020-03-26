class MyQueue:
    def __init__(self):
        self.queue = []
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(10)
    # param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    # print(param_2)
    print(param_3)
    print(param_4)
