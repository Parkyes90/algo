from typing import List


class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        maximum = max(candies)
        ret = []
        for candy in candies:
            ret.append(candy + extraCandies >= maximum)
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.kidsWithCandies([4, 2, 1, 1, 2], 1)
    print(answer)
