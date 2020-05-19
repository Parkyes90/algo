from typing import List
from itertools import combinations


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        indexes = [i for i in range(len(rating))]
        combs = combinations(indexes, 3)
        count = 0
        for comb in combs:
            i, j, k = comb
            if rating[i] > rating[j] > rating[k]:
                count += 1

            elif rating[i] < rating[j] < rating[k]:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.numTeams([1, 2, 3, 4])
    print(answer)
