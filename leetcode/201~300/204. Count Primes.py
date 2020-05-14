from math import sqrt


class Solution:
    def is_prime(self, num):
        if num < 2:
            return False
        if num < 4:
            return True

        if num % 2 == 0:
            return False

        for i in range(3, int(sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(n):
            if self.is_prime(i):
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.countPrimes(10)
    print(answer)
