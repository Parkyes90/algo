class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if i % 2 == 0:
                ans += s[i]
            else:
                character = s[i - 1]
                digit = s[i]
                ans += chr(ord(character) + int(digit))
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.replaceDigits("a1c1e1")
    assert answer == "abcdef"
