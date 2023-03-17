class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = ""
        second = ""
        target = ""

        for letter in firstWord:
            first += str(ord(letter) - 97)

        for letter in secondWord:
            second += str(ord(letter) - 97)

        for letter in targetWord:
            target += str(ord(letter) - 97)

        return int(first) + int(second) == int(target)


if __name__ == "__main__":
    s = Solution()
    assert s.isSumEqual("acb", "cba", "cdb") is True
    assert s.isSumEqual("aaa", "a", "aab") is False
    assert s.isSumEqual("aaa", "a", "aaaa") is True
