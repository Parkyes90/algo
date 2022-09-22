class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            word = words[i]
            words[i] = word[::-1]
        return " ".join(words)


if __name__ == "__main__":
    s = Solution()
    answer = s.reverseWords("Let's take LeetCode contest")
    assert answer == "s'teL ekat edoCteeL tsetnoc"
