from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = {}

    def sumRange(self, i: int, j: int) -> int:
        if (i, j) not in self.cache:
            ret = 0
            for index in range(i, j + 1):
                ret += self.nums[index]
            self.cache[(i, j)] = ret
        return self.cache[(i, j)]


# Your NumArray object will be instantiated and called as such:
if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    param_1 = obj.sumRange(0, 2)
    param_2 = obj.sumRange(2, 5)
    print(param_1)
    print(obj.cache)
