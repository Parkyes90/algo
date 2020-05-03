from typing import List
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # number validation
        ret = -1
        for h1, h2, m1, m2 in permutations(A):
            hour = 10 * h1 + h2
            minute = 10 * m1 + m2
            t = 60 * hour + minute
            if 0 <= hour < 24 and 0 <= minute < 60 and t > ret:
                ret = t
        if ret < 0:
            return ""
        val, remain = divmod(ret, 60)
        return "{:02}:{:02}".format(val, remain)


if __name__ == "__main__":
    s = Solution()
    answer = s.largestTimeFromDigits([2, 0, 6, 6])
    print(answer)
