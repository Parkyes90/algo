from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)


if __name__ == "__main__":
    s = Solution()
    answer = s.canBeEqual([1, 2, 2, 3], [1, 1, 2, 3])
    print(answer)
