class Solution:
    """https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/submissions/"""

    def generateTheString(self, n: int) -> str:
        ans = ""
        if n % 2 == 0:
            ans += "a" * (n - 1)
            ans += "b"
        else:
            ans += "a" * n
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.generateTheString(4)
    print(answer)
