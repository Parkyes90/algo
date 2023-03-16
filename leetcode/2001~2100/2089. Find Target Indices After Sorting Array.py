from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.targetIndices([1, 2, 5, 2, 3], 2) == [1, 2]
    assert s.targetIndices([1, 2, 5, 2, 3], 3) == [3]
    assert s.targetIndices([1, 2, 5, 2, 3], 5) == [4]
