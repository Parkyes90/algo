class Solution:
    def countDigits(self, num: int) -> int:
        result = 0
        for n in str(num):
            if num % int(n) == 0:
                result += 1
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.countDigits(7) == 1
    assert s.countDigits(121) == 2
