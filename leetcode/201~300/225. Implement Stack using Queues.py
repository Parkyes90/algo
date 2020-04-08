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
        return self.data.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.data:
            return self.data[-1]
        return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data) < 1


# Your MyStack object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyStack()
    obj.push(5)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)
