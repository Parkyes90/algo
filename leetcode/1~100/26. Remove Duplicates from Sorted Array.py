from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                del nums[index]
            else:
                index += 1
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    answer = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(answer)
