from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        w2 = ""
        for piece in word1:
            w1 += piece
        for piece in word2:
            w2 += piece
        return w1 == w2


if __name__ == "__main__":
    s = Solution()
    answer = s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
    assert answer is True
