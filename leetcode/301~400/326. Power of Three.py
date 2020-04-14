import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        re_calc = math.pow(3, int(math.log2(n) / math.log2(3)))
        return re_calc == n


if __name__ == "__main__":
    s = Solution()
    answer = s.isPowerOfThree(243)
    print(answer)
