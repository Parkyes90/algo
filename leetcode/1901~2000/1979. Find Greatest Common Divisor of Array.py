from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        for i in range(max_num, 0, -1):
            if max_num % i == 0 and min_num % i == 0:
                return i


if __name__ == "__main__":
    s = Solution()
    assert s.findGCD([2, 5, 6, 9, 10]) == 2
    assert s.findGCD([7, 5, 6, 8, 3]) == 1
    assert s.findGCD([3, 3]) == 3
