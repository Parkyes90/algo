from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i * j % k == 0:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.countPairs([3, 1, 2, 2, 2, 1, 3], 2)
    assert answer == 4
