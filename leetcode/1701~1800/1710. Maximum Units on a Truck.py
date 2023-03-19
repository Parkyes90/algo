from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        answer = 0
        for box_type in boxTypes:
            if truckSize <= box_type[0]:
                answer += truckSize * box_type[1]
                return answer
            else:
                answer += box_type[0] * box_type[1]
                truckSize -= box_type[0]
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.maximumUnits([[1, 3], [2, 2], [3, 1]], 4) == 8
    assert s.maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10) == 91
