from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        _sum = 0
        for key, value in counter.items():
            if value == 1:
                _sum += key
        return _sum


if __name__ == "__main__":
    s = Solution()
    assert s.sumOfUnique([1, 2, 3, 2]) == 4
    assert s.sumOfUnique([1, 1, 1, 1, 1]) == 0
    assert s.sumOfUnique([1, 2, 3, 4, 5]) == 15
