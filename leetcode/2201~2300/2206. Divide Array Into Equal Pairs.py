from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i + 1]:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.divideArray([3, 2, 3, 2, 2, 2]) is True
    assert s.divideArray([1, 2, 3, 4]) is False
