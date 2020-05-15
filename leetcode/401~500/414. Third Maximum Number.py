from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        if len(unique_nums) < 3:
            return max(unique_nums)
        maximum = unique_nums[0]
        for i in range(3):
            maximum = max(unique_nums)
            maximum_index = unique_nums.index(maximum)
            del unique_nums[maximum_index]
        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.thirdMax([2, 2, 3, 1])
    print(answer)
