from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if s.startswith(word):
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc") == 3
    assert s.countPrefixes(["a", "a"], "aa") == 2
