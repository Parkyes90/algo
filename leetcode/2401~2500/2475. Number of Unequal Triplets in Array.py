from collections import Counter
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

    def unequalTriplets2(self, nums: List[int]) -> int:

        counter = Counter(nums)
        ret = 0

        left = 0
        right = len(nums)

        for freq in counter.values():
            right -= freq
            ret += left * right * freq
            left += freq
        return ret


if __name__ == "__main__":
    assert Solution().unequalTriplets2([4, 4, 2, 4, 3]) == 3
    assert Solution().unequalTriplets2([1, 1, 1, 1, 1]) == 0
