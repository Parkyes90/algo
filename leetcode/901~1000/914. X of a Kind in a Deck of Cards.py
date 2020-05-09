import math
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vals = Counter(deck).values()
        return reduce(math.gcd, vals) >= 2


if __name__ == "__main__":
    s = Solution()
    answer = s.hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])
    print(answer)
