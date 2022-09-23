from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.numOfStrings(["a", "abc", "bc", "d"], "abc")
    assert answer == 3
