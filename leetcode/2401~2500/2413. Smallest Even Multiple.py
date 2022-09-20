class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n * 2


if __name__ == "__main__":
    s = Solution()
    answer = s.smallestEvenMultiple(5)
    assert answer == 10
