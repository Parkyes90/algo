from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        right_sum = sum(nums)
        left_sum = 0
        nums_length = len(nums)
        for i in range(0, nums_length):
            if i > 0:
                left_sum += nums[i - 1]
                right_sum -= nums[i - 1]
            if left_sum == right_sum - nums[i]:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    answer = s.pivotIndex([-1, -1, -1, 0, 1, 1])
    print(answer)
