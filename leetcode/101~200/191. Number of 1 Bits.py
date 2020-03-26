class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


if __name__ == "__main__":
    s = Solution()
    answer = s.hammingWeight(9)
    print(answer)
