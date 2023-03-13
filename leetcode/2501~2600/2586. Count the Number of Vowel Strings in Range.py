from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = {"a", "e", "i", "o", "u"}
        for i in range(left, right + 1):
            word = words[i]
            start = word[0]
            end = word[-1]

            if start in vowels and end in vowels:
                count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.vowelStrings(["are", "amy", "u"], 0, 2) == 2
    assert s.vowelStrings(["hey", "aeo", "mu", "ooo", "artro"], 1, 4) == 3
