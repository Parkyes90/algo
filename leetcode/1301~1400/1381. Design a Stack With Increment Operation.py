class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.current_size = 0
        self.data = []

    def push(self, x: int) -> None:
        if self.current_size < self.max_size:
            self.data.append(x)
            self.current_size += 1

    def pop(self) -> int:
        if not self.data:
            return -1
        self.current_size -= 1
        return self.data.pop()

    def increment(self, k: int, val: int) -> None:
        apply_range = k if k < len(self.data) else len(self.data)
        for i in range(apply_range):
            self.data[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

if __name__ == "__main__":
    s = CustomStack(5)
