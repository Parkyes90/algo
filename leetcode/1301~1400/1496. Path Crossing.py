class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction_map = {"N": 1, "E": 1, "S": -1, "W": -1}
        start = (0, 0)
        visits = {start}
        for p in path:

            x, y = start
            direction = direction_map[p]
            if p in {"N", "S"}:
                y += direction
            else:
                x += direction
            start = (x, y)
            if start in visits:
                return True
            visits.add(start)

        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.isPathCrossing("NESWW")
    print(answer)
