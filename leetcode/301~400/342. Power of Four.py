import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        log_val = math.log2(num) / math.log2(4)
        return log_val == int(log_val)


if __name__ == "__main__":
    s = Solution()
    answer = s.isPowerOfFour(0)
    print(answer)
