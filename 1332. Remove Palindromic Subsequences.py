class Solution:
    """https://leetcode.com/problems/remove-palindromic-subsequences/"""

    def is_palindrome(self, s):
        return s == s[::-1]

    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0

        return 1 if self.is_palindrome(s) else 2


if __name__ == "__main__":
    s = Solution()
    answer = s.removePalindromeSub("baabb")
    print(answer)
