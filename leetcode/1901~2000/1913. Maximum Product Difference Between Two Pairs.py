from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        rank_1 = max(nums)
        nums.remove(rank_1)
        rank_2 = max(nums)
        reverse_rank_1 = min(nums)
        nums.remove(reverse_rank_1)
        reverse_rank_2 = min(nums)
        return (rank_1 * rank_2) - (reverse_rank_1 * reverse_rank_2)


if __name__ == "__main__":
    s = Solution()
    answer = s.maxProductDifference([5, 6, 2, 7, 4])
    assert answer == 34
