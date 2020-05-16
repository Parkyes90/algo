from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if p is not None:
                    return False
                p = i

        if p is None:
            return True

        if p == 0:
            return True

        if p == len(nums) - 2:
            return True

        if nums[p - 1] <= nums[p + 1]:
            return True

        if nums[p] <= nums[p + 2]:
            return True

        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.checkPossibility([3, 4, 2, 3])
    print(answer)
