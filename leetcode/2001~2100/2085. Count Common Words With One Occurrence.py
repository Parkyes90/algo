from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ret = 0
        words1_counter = Counter(words1)
        words2_counter = Counter(words2)

        for key, value in words1_counter.items():
            if value == 1 and words2_counter.get(key) and words2_counter[key] == 1:
                ret += 1

        return ret


if __name__ == "__main__":
    assert (
        Solution().countWords(
            ["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]
        )
        == 2
    )

    assert Solution().countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"]) == 0
    assert Solution().countWords(["a", "ab"], ["a", "a", "a", "ab"]) == 1
