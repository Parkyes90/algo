class Solution:
    def sqrt(self, num: int):
        n = num
        for i in range(100):
            n = (n + (num / n)) / 2
        return n

    def isPerfectSquare(self, num: int) -> bool:
        square = self.sqrt(num)
        return square == int(square)


if __name__ == "__main__":
    s = Solution()
    answer = s.isPerfectSquare(808201)
    print(answer)
