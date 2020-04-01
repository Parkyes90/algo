from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count_map = {}
        maximum = 0
        for n in nums:
            if n not in count_map:
                count_map[n] = 1
            else:
                count_map[n] += 1
            if count_map.get(n + 1):
                maximum = max(maximum, count_map[n] + count_map[n + 1])
            if count_map.get(n - 1):
                maximum = max(maximum, count_map[n] + count_map[n - 1])

        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.findLHS([1, 3, 2, 2, 5, 2, 3, 7])
    print(answer)
