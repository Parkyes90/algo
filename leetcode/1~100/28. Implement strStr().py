class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)


if __name__ == "__main__":
    s = Solution()
    answer = s.strStr("hello", "ll")
    print(answer)
