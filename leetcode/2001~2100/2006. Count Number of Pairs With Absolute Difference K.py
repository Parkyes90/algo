from typing import List
from itertools import combinations


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        combs = combinations(nums, 2)
        count = 0
        for comb in combs:
            if abs(comb[0] - comb[1]) == k:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.countKDifference([1, 2, 2, 1], 1) == 4
