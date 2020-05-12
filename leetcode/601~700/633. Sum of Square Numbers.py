from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i * i <= c:
            remain = c - i * i
            sq = sqrt(remain)
            if sq == int(sq):
                return True
            i += 1
        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.judgeSquareSum(3)
    print(answer)
