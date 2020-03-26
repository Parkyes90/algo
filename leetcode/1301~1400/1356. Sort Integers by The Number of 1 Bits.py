from typing import List


class Solution:
    """
    https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
    """

    def count_binary_one(self, n):
        count = 0
        while n > 0:
            n, remain = divmod(n, 2)
            if remain == 1:
                count += 1
        return count

    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (self.count_binary_one(x), x))
        return arr


if __name__ == "__main__":
    s = Solution()
    answer = s.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8])

    print(answer)
