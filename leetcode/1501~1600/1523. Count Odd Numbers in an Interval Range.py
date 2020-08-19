class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2

        return (high - low) // 2 + 1


if __name__ == "__main__":
    s = Solution()
    answer = s.countOdds(5, 11)
    print(answer)
