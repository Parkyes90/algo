from typing import List


class KthLargest:
    """https://leetcode.com/problems/kth-largest-element-in-a-stream/"""

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)[:k]
        self.k = k

    def binary_search(self, target: int):
        left = 0
        right = len(self.nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] < target:
                right = mid - 1
            elif self.nums[mid] > target:
                left = mid + 1
            else:
                return mid
        return left

    def add(self, val: int) -> int:
        index = self.binary_search(val)
        self.nums.insert(index, val)
        self.nums = self.nums[: self.k]
        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
