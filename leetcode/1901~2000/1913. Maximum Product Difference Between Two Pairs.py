from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        return (nums[length - 1] * nums[length - 2]) - (nums[0] * nums[1])


if __name__ == "__main__":
    s = Solution()
    answer = s.maxProductDifference([5, 6, 2, 7, 4])
    assert answer == 34
