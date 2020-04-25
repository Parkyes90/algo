class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while (i ** 2 + i) / 2 <= n:
            i += 1
        return i - 1


if __name__ == "__main__":
    s = Solution()
    answer = s.arrangeCoins(2)
    print(answer)
