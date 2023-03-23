from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            _max = max(nums)
            if _max == 0:
                return count
            count += 1
            _min = min([n for n in nums if n > 0])
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= _min

    def minimumOperations2(self, nums: List[int]) -> int:
        return len({num for num in nums if num != 0})


if __name__ == "__main__":
    s = Solution()
    assert s.minimumOperations([1, 5, 0, 3, 5]) == 3
    assert s.minimumOperations([0]) == 0
