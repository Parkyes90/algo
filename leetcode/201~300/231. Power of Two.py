class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power_of_two = 2 ** 0
        while power_of_two <= n:
            if power_of_two == n:
                return True
            power_of_two *= 2
        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.isPowerOfTwo(2049)
    print(answer)
