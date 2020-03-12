from typing import List


class Solution:
    """https://leetcode.com/problems/unique-number-of-occurrences/"""

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}
        for a in arr:
            if a not in count_map:
                count_map[a] = 1
            else:
                count_map[a] += 1

        count_map_values = count_map.values()

        return len(count_map_values) == len(set(count_map_values))


if __name__ == "__main__":
    s = Solution()
    answer = s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
    print(answer)
