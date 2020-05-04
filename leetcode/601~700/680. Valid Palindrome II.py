class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        length = len(s)
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                j = length - 1 - i
                return is_palindrome(i + 1, j) or is_palindrome(i, j - 1)

        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.validPalindrome("abaaabaa")
    print(answer)
