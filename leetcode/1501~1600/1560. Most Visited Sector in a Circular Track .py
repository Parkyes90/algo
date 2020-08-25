from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        count_map = {i: 0 for i in range(1, n + 1)}
        count_map[rounds[0]] += 1
        for i in range(1, len(rounds)):
            start = rounds[i - 1]
            end = rounds[i]
            length = end - start
            if length < 0:
                length = n - start + end

            for j in range(length):
                sector = start + j + 1
                if sector > n:
                    sector = sector - n
                count_map[sector] += 1
        maximum = max(count_map.values())
        ret = []
        for key, value in count_map.items():
            if value == maximum:
                ret.append(key)
        ret.sort()
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.mostVisited(4, [1, 3, 1, 2]))
