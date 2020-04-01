from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count_map = {}
        for n in nums:
            if n not in count_map:
                count_map[n] = 1
            else:
                count_map[n] += 1
        count_keys = sorted(count_map.keys())
        combinations = []
        for i in range(len(count_keys) - 1):
            if count_keys[i + 1] - count_keys[i] < 2:
                combinations.append((count_keys[i], count_keys[i + 1]))

        if not combinations:
            return 0
        maximum = 0
        for combination in combinations:
            key1, key2 = combination
            if count_map[key1] + count_map[key2] > maximum:
                maximum = count_map[key1] + count_map[key2]

        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.findLHS([1, 3, 2, 2, 5, 2, 3, 7])
    print(answer)
