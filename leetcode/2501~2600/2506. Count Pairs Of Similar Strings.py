from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        for i in range(len(words)):
            words[i] = set(words[i])
        count = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]) == 2
    assert s.similarPairs(["aabb", "ab", "ba"]) == 3
    assert s.similarPairs(["nba", "cba", "dba"]) == 0
