from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maximum = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                length = 1
            if maximum < length:
                maximum = length
        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.findLengthOfLCIS([2, 1, 3, 2, 2, 3, 4, 5])
    print(answer)
