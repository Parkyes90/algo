from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            remainder = i % 10
            if remainder == nums[i]:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().smallestEqual([0, 1, 2]) == 0
    assert Solution().smallestEqual([4, 3, 2, 1]) == 2
    assert Solution().smallestEqual([7, 8, 3, 5, 2, 6, 3, 1, 1, 4, 5, 4, 8, 7, 2, 0, 9, 9, 0, 5, 7, 1, 6]) == 21
