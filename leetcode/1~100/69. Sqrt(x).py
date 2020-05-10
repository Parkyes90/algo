class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        while n * n <= x:
            n += 1
        return n - 1


if __name__ == "__main__":
    s = Solution()
    answer = s.mySqrt(9)
    print(answer)
