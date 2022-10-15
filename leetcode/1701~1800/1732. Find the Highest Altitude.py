from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        for i in gain:
            current_altitude += i
            max_altitude = max(max_altitude, current_altitude)
        return max_altitude


if __name__ == "__main__":
    s = Solution()
    s.largestAltitude([-5, 1, 5, 0, -7])
