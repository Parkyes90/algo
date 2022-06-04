from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(str)
        result = 0
        for i in range(len(rings) // 2):
            color, rod = rings[i * 2 : i * 2 + 2]
            rods[rod] += color
        for colors in rods.values():
            if len(set(colors)) == 3:
                result += 1
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.countPoints("B0B6G0R6R0R6G9") == 1
