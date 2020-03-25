from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    answer = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
