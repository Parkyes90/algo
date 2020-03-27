from typing import List


class Solution:
    def createTargetArray(
        self, nums: List[int], index: List[int]
    ) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.insert(index[i], nums[i])
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
    print(answer)
