from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            if ret + nums[i] < nums[i]:
                ret = nums[i]
            else:
                ret += nums[i]
            if ret > maximum:
                maximum = ret
        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.maxSubArray([1, 2])
    print(answer)
