from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        num_set = set(nums)
        for num in nums:
            remaining = num - diff
            next_to_find = num + diff

            if remaining in num_set and next_to_find in nums:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3)
    assert answer == 2
