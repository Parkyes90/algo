from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0

        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        return max(pos, neg)

    def maximumCountByBisect(self, nums: List[int]) -> int:

        pos = bisect_left(nums, 0)
        neg = len(nums) - bisect_right(nums, 0)
        return max(pos, neg)


if __name__ == "__main__":
    s = Solution()
    assert s.maximumCountByBisect([5, 20, 66, 1314]) == 4
    assert s.maximumCountByBisect([-2, -1, -1, 1, 2, 3]) == 3
    assert s.maximumCountByBisect([-3, -2, -1, 0, 0, 1, 2]) == 3
