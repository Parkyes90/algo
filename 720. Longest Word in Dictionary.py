import collections
from functools import reduce
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        words.sort(key=lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in word_set for k in range(1, len(word))):
                return word

        return ""


if __name__ == "__main__":
    s = Solution()
    answer = s.longestWord(
        [
            "yo",
            "ew",
            "fc",
            "zrc",
            "yodn",
            "fcm",
            "qm",
            "qmo",
            "fcmz",
            "z",
            "ewq",
            "yod",
            "ewqz",
            "y",
        ]
    )
    print(answer)
