from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = sum(nums[:k])
        current = maximum
        for i in range(k, len(nums)):
            current = current - nums[i - k] + nums[i]
            if current > maximum:
                maximum = current
        return maximum / k


if __name__ == "__main__":
    s = Solution()
    answer = s.findMaxAverage([1, 2, 5], 2)
    print(answer)
