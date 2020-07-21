class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = numBottles
        maximum = numBottles
        while empty_bottles >= numExchange:
            value, remain = divmod(empty_bottles, numExchange)
            maximum += value
            empty_bottles = value + remain
        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.numWaterBottles(15, 4)
    print(answer)
