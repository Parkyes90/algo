class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ""
        index = 0
        length = len(s)
        while index < length - 1:
            first = s[index]
            second = s[index + 1]
            if first != second and first.lower() == second.lower():
                s = s[:index] + s[index + 2 :]
                index = 0
                length = len(s)
                continue
            index += 1
        return s


if __name__ == "__main__":
    s = Solution()
    answer = s.makeGood("s")
    print(answer)
