from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count_map = {}
        lucky_list = []
        for a in arr:
            if a not in count_map:
                count_map[a] = 1
            else:
                count_map[a] += 1
        for key, value in count_map.items():
            if key == value:
                lucky_list.append(key)
        if not lucky_list:
            return -1
        return max(lucky_list)


if __name__ == "__main__":
    s = Solution()
    answer = s.findLucky([1, 2, 2, 3, 3, 3])
    print(answer)
