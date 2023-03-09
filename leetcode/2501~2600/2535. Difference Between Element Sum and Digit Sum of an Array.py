from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            for n in str(num):
                digit_sum += int(n)
        return abs(element_sum - digit_sum)


if __name__ == "__main__":
    s = Solution()
    assert s.differenceOfSum([1, 15, 6, 3]) == 9
    assert s.differenceOfSum([1, 2, 3, 4]) == 0
