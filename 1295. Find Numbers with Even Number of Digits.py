from typing import List


class Solution:
    """https://leetcode.com/problems/find-numbers-with-even-number-of-digits/"""

    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            digits = len(str(num))
            if digits % 2 == 0:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.findNumbers([555, 901, 482, 1771])
    print(result)
