from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


if __name__ == "__main__":
    s = Solution()
    answer1 = s.convertTemperature(36.50)
    assert answer1 == [309.65000, 97.70000]
