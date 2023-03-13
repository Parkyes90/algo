from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for n in str(num):
                result.append(int(n))
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.separateDigits([13, 25, 83, 77]) == [1, 3, 2, 5, 8, 3, 7, 7]
    assert s.separateDigits([7, 1, 3, 9]) == [7, 1, 3, 9]
