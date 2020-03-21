class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        listed_s = list(s)
        for i in range(0, len(listed_s), 2 * k):
            listed_s[i : i + k] = reversed(listed_s[i : i + k])
        return "".join(listed_s)


if __name__ == "__main__":
    s = Solution()
    answer = s.reverseStr("abcdefg", 2)
    print(answer)
