from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.numIdenticalPairs([1, 2, 3, 1, 1, 3])
    print(answer)
