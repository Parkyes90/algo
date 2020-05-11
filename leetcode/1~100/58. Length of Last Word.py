class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listed = s.split(" ")
        length = len(listed)
        for i in range(length - 1, -1, -1):
            if listed[i]:
                return len(listed[i])
        return 0


if __name__ == "__main__":
    s = Solution()
    answer = s.lengthOfLastWord("Hello World")
    print(answer)
