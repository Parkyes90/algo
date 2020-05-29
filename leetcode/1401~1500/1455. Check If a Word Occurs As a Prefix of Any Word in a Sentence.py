class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        listed = sentence.split(" ")
        for i in range(len(listed)):
            if listed[i].startswith(searchWord):
                return i + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    answer = s.isPrefixOfWord("hello from the other side", "they")
    print(answer)
