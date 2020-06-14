from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices


if __name__ == "__main__":
    s = Solution()
    answer = s.finalPrices([10, 1, 1, 6])
    print(answer)
