from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.counter = defaultdict(int)

    def set_counter(self, nums):
        for num in set(nums):
            self.counter[num] += 1

    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        for nums in [nums1, nums2, nums3]:
            self.set_counter(nums)
        return [key for key, value in self.counter.items() if value > 1]


if __name__ == "__main__":
    assert Solution().twoOutOfThree([1, 1, 3, 2], [2, 3], [3]) == [2, 3]
    assert Solution().twoOutOfThree([3, 1], [2, 3], [1, 2]) == [1, 3, 2]
    assert Solution().twoOutOfThree([1, 2, 2], [4, 3, 3], [5]) == []
