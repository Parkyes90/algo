from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = max(nums)
        maximum_index = nums.index(maximum)
        for i in range(len(nums)):
            if i == maximum_index:
                continue
            if nums[i] * 2 > maximum:
                return -1
        return maximum_index


if __name__ == "__main__":
    s = Solution()
    answer = s.dominantIndex([1, 2, 3, 4])
    print(answer)
