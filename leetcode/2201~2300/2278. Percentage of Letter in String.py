class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:

        return int(s.count(letter) / len(s) * 100)


if __name__ == "__main__":
    s = Solution()
    assert s.percentageLetter("foobar", "o") == 33
    assert s.percentageLetter("jjjj", "k") == 0
