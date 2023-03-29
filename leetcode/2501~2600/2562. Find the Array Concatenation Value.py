from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = 0
        while left <= right:
            if left == right:
                ans += nums[left]
            else:
                ans += int(f"{nums[left]}{nums[right]}")
            left += 1
            right -= 1
        return ans


if __name__ == "__main__":
    assert Solution().findTheArrayConcVal([7, 52, 2, 4]) == 596
    assert Solution().findTheArrayConcVal([5, 14, 13, 8, 12]) == 673
