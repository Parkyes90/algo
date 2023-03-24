class Solution:
    def minTimeToType(self, word: str) -> int:
        word = f"a{word}"
        seconds = 0
        for index in range(1, len(word)):
            clockwise_distance = abs(ord(word[index - 1]) - ord(word[index]))
            if clockwise_distance > 12:
                seconds += 25 - clockwise_distance + 1
            else:
                seconds += clockwise_distance

            seconds += 1
        return seconds


if __name__ == "__main__":
    s = Solution()
    assert s.minTimeToType("abc") == 5
    assert s.minTimeToType("bza") == 7
    assert s.minTimeToType("zjpc") == 34
    assert s.minTimeToType("pdy") == 31
