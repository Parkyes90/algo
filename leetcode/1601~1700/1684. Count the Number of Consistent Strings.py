from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        for word in words:
            is_consistent = True
            for letter in word:
                if letter not in allowed_set:
                    is_consistent = False
                    break
            if is_consistent:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    ans = s.countConsistentStrings(
        allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]
    )
    assert ans == 2
