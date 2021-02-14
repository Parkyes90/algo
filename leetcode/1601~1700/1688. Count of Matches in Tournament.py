class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


if __name__ == "__main__":
    s = Solution()
    for i in range(1, 200):
        answer = s.numberOfMatches(i)
        print(answer, i)
