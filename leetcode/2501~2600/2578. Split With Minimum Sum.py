class Solution:
    def splitNum(self, num: int) -> int:
        digits = list(str(num))
        digits.sort()
        left = int("".join(digits[0::2]))
        right = int("".join(digits[1::2]))
        return left + right


if __name__ == "__main__":
    assert Solution().splitNum(100001) == 2
    assert Solution().splitNum(4325) == 59
    assert Solution().splitNum(687) == 75
    assert Solution().splitNum(101) == 2
    assert Solution().splitNum(91) == 10
    assert Solution().splitNum(11) == 2
    assert Solution().splitNum(123456789) == 16047
    assert Solution().splitNum(999999999) == 109998
