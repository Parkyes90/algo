from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        compare = sorted(nums)
        start = len(nums)
        end = 0
        for i in range(len(nums)):
            if nums[i] != compare[i]:
                start = min(start, i)
                end = max(end, i)

        if end - start < 0:
            return 0
        return end - start + 1


if __name__ == "__main__":
    s = Solution()
    answer = s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 11, 15, 15])
    print(answer)
