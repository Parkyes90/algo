from typing import List
from itertools import combinations


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = 0
        combs = combinations((i for i in range(len(nums))), 2)
        for comb in combs:
            i, j = comb
            temp = (nums[i] - 1) * (nums[j] - 1)
            if temp > ret:
                ret = temp
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.maxProduct([3, 4, 5, 2])
    print(answer)
