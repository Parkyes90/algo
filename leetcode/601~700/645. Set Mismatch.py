from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        maximum = len(nums)
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        ret = []
        for i in range(1, maximum + 1):
            if i in nums_map and nums_map[i] > 1:
                ret.append(i)
        for i in range(1, maximum + 1):
            if i not in nums_map:
                ret.append(i)
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.findErrorNums([2, 2])
    print(answer)
