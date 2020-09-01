from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    s = Solution()
    answer = s.permute([1, 2, 3])
    assert answer == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
