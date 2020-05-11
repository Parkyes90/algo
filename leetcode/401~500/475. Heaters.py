from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        heaters.append(float("inf"))
        index = 0
        radius = 0
        for house in houses:
            while house >= heaters[index]:
                index += 1
            radius = max(
                radius,
                min(abs(house - heaters[index - 1]), heaters[index] - house),
            )
        return radius


if __name__ == "__main__":
    s = Solution()
    answer = s.findRadius(
        [
            282475249,
            622650073,
            984943658,
            144108930,
            470211272,
            101027544,
            457850878,
            458777923,
        ],
        [
            823564440,
            115438165,
            784484492,
            74243042,
            114807987,
            137522503,
            441282327,
            16531729,
            823378840,
            143542612,
        ],
    )
    print(answer)
