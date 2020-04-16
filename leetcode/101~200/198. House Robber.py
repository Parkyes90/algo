from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) < 2:
            return dp[-1]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    answer = s.rob([2, 3, 4, 5])
    print(answer)
