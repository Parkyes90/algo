class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "i", "e", "o", "u"}
        listed = list(s)
        temp = []
        indexes = []
        for i in range(len(listed)):
            if s[i].lower() in vowels:
                indexes.append(i)
                temp.append(s[i])
        temp.reverse()
        for i in range(len(indexes)):
            listed[indexes[i]] = temp[i]
        return "".join(listed)


if __name__ == "__main__":
    s = Solution()
    answer = s.reverseVowels("aA")
    print(answer)
