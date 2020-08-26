from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        length = len(piles) // 3
        total = 0
        for i in range(1, length * 2, 2):
            total += piles[i]
        return total


if __name__ == "__main__":
    s = Solution()
    answer = s.maxCoins([2, 4, 1, 2, 7, 8])
    print(answer)
