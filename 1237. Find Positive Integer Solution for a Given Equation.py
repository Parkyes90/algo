"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
from typing import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x + y


class Solution:
    """https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/"""

    def findSolution(
        self, customfunction: CustomFunction, z: int
    ) -> List[List[int]]:
        ret = []
        for x in range(1, 1001):
            for y in range(1, 1001):
                if customfunction.f(x, y) > z:
                    break

                if customfunction.f(x, y) == z:
                    ret.append([x, y])
        return ret


if __name__ == "__main__":
    s = Solution()
    func = CustomFunction()
    answer = s.findSolution(func, 5)
    print(answer)
