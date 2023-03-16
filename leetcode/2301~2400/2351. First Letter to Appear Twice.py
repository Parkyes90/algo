from collections import defaultdict


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counter = defaultdict(int)

        for letter in s:
            counter[letter] += 1
            if counter[letter] == 2:
                return letter

        raise ValueError("No repeated character")


if __name__ == "__main__":
    s = Solution()
    assert s.repeatedCharacter("abccbaacz") == "c"
    assert s.repeatedCharacter("abcdd") == "d"
