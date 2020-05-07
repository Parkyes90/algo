class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        alpha = set()
        for i in range(0, 10):
            alpha.add(str(i))
        for i in range(ord("a"), ord("z") + 1):
            alpha.add(chr(i))
        for i in range(ord("A"), ord("Z") + 1):
            alpha.add(chr(i))
        ans = ""
        for a in s:
            if a in alpha:
                ans += a.lower()
        return ans == ans[::-1]


if __name__ == "__main__":
    s = Solution()
    answer = s.isPalindrome("0P")
    print(answer)
