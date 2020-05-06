class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
        total = 0
        n = 1
        while n * n <= num:
            if num % n == 0:
                total += n
                if n * n != num:
                    total += num / n
            n += 1
        return total - num == num


if __name__ == "__main__":
    s = Solution()
    answer = s.checkPerfectNumber(2)
    print(answer)
