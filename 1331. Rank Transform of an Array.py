from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """https://leetcode.com/problems/rank-transform-of-an-array/submissions/"""
        count_map = {}
        for a in arr:
            if a not in count_map:
                count_map[a] = 0
        for rank, key in enumerate(sorted(count_map.keys()), 1):
            count_map[key] = rank
        ret = []
        for a in arr:
            ret.append(count_map[a])
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.arrayRankTransform([40, 10, 20, 30])
    print(answer)
