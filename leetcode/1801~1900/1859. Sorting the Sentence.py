class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        words.sort(key=lambda word: int(word[len(word) - 1]))
        return " ".join([word[:-1] for word in words])


if __name__ == "__main__":
    s = Solution()
    answer = s.sortSentence("is2 sentence4 This1 a3")
    print(answer)
