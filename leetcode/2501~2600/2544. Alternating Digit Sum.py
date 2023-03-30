class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = list(str(n))
        ans = 0
        for i in range(len(digits)):
            if i % 2 == 0:
                ans += int(digits[i])
            else:
                ans -= int(digits[i])
        return ans


if __name__ == "__main__":
    assert Solution().alternateDigitSum(521) == 4
    assert Solution().alternateDigitSum(111) == 1
    assert Solution().alternateDigitSum(886996) == 0
