from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        times = [0, *releaseTimes]
        maximum = 0
        for i in range(1, len(times)):
            duration = times[i] - times[i - 1]
            if duration > maximum:
                maximum = duration
        indexes = []
        for i in range(1, len(times)):
            duration = times[i] - times[i - 1]
            if duration == maximum:
                indexes.append(i - 1)
        keys = []
        for i in indexes:
            keys.append(keysPressed[i])
        keys.sort(reverse=True)
        return keys[0]


if __name__ == "__main__":
    s = Solution()
    answer = s.slowestKey([9, 29, 49, 50], "cbcd")
    assert answer == "c"
