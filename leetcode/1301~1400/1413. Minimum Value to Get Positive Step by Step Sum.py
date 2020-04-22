from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current = nums[0]
        minimum = current
        for i in range(1, len(nums)):
            current += +nums[i]
            if current < minimum:
                minimum = current
        if minimum > 0:
            return 1
        return abs(minimum) + 1


if __name__ == "__main__":
    s = Solution()
    answer = s.minStartValue([1, 2])
    print(answer)
