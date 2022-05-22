class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


if __name__ == "__main__":
    s = Solution()
    result1 = s.sum(-10, -6)
    assert result1 == -16
