from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.prefixCount(["pay", "attention", "practice", "attend"], "at") == 2
    assert s.prefixCount(["leetcode", "win", "loops", "success"], "code") == 0
