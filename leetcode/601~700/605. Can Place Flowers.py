from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n < 1:
            return True
        index = 0

        while index < len(flowerbed):
            is_flower = flowerbed[index]
            if is_flower:
                index += 2
                continue
            is_flower_plus = False
            if index + 1 < len(flowerbed):
                is_flower_plus = flowerbed[index + 1] == 1
            if is_flower_plus:
                index += 5
                continue
            else:
                flowerbed[index] = 1
                index += 2
                n -= 1
                if n == 0:
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.canPlaceFlowers([0, 0, 1, 0, 0], 1)
    print(answer)
