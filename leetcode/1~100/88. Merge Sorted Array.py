from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = m
        for i in range(start, m + n):
            nums1[i] = nums2[i - start]
        nums1.sort()


if __name__ == "__main__":
    nums = [1, 2, 3, 0, 0, 0]
    s = Solution()
    s.merge(nums, 3, [2, 5, 6], 3)
    print(nums)
