from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            target_index = nums[i]
            target_value = nums[target_index]
            ans.append(target_value)
        return ans


if __name__ == "__main__":
    s = Solution()
    result = s.buildArray([0, 2, 1, 5, 3, 4])
    print(result)
