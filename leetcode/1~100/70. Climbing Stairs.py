class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 2] + dp[i - 1])
        return dp[n - 1]


if __name__ == "__main__":
    s = Solution()
    answer = s.climbStairs(5)
    print(answer)
