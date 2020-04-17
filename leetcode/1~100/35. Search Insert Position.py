from typing import List


class Solution:
    def binary_search(self, nums: List[int], target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)


if __name__ == "__main__":
    s = Solution()
    answer = s.searchInsert([1], 1)
    print(answer)
