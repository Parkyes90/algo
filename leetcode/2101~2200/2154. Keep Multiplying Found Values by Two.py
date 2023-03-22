from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        while True:
            if original not in nums_set:
                return original

            original *= 2


if __name__ == "__main__":
    s = Solution()
    assert s.findFinalValue([5, 3, 6, 1, 12], 3) == 24
    assert s.findFinalValue([2, 7, 9], 4) == 4
