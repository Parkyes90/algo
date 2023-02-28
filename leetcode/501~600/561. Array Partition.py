from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    s = Solution()
    assert s.arrayPairSum([1, 4, 3, 2]) == 4
    assert s.arrayPairSum([6, 2, 6, 5, 1, 2]) == 9
