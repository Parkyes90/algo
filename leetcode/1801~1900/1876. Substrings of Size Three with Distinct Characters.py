class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = 0

        for i in range(len(s) - 2):
            substring = s[i : i + 3]
            if len(substring) == len(set(substring)):
                count += 1
        return count


if __name__ == "__main__":
    assert Solution().countGoodSubstrings("xyzzaz") == 1
    assert Solution().countGoodSubstrings("aababcabc") == 4
