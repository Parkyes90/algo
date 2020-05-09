from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        copy_nums = nums.copy()
        k = k % length
        for i in range(length):
            rotate_index = (i + k) % length
            nums[rotate_index] = copy_nums[i]


if __name__ == "__main__":
    arr = [-1, -100, 3, 99]

    s = Solution()
    s.rotate(arr, 2)
