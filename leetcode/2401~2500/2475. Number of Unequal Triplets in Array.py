from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        count += 1

        return count


if __name__ == "__main__":
    assert Solution().unequalTriplets([4, 4, 2, 4, 3]) == 3
    assert Solution().unequalTriplets([1, 1, 1, 1, 1]) == 0
