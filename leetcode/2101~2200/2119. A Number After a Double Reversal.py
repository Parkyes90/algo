class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num < 10:
            return True

        if str(num)[::-1].startswith("0"):
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isSameAfterReversals(526) is True
    assert s.isSameAfterReversals(1800) is False
    assert s.isSameAfterReversals(0) is True
