from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        count = 0
        for i in range(len(nums) - 1):
            current, _next = nums[i], nums[i + 1]
            if _next <= current:
                increment = current - +_next + 1
                nums[i + 1] += increment
                count += increment
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.minOperations([1, 1, 1]) == 3
    assert s.minOperations([1, 5, 2, 4, 1]) == 14
    assert s.minOperations([8]) == 0
