from typing import List, Union


class Solution:
    """https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/"""

    def getNoZeroIntegers(self, n: int) -> List[Union[int, None]]:
        for i in range(1, n):
            if str(i).find("0") < 0 and str(n - i).find("0") < 0:
                return [i, n - i]
        return [None, None]


if __name__ == "__main__":
    s = Solution()
    answer = s.getNoZeroIntegers(1010)
    print(answer)
