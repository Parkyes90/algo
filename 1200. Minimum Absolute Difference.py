from typing import List


class Solution:
    """https://leetcode.com/problems/minimum-absolute-difference/"""

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        for i in range(len(arr) - 1):
            absolute_diff = abs(arr[i] - arr[i + 1])
            if abs(absolute_diff) < min_diff:
                min_diff = absolute_diff
        ret = []
        for i in range(len(arr) - 1):
            absolute_diff = abs(arr[i] - arr[i + 1])
            if absolute_diff == min_diff:
                ret.append([arr[i], arr[i + 1]])
        return ret


if __name__ == "__main__":
    s = Solution()
    ans = s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27])
    print(ans)
