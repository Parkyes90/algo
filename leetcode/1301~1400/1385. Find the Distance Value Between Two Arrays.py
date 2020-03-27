from typing import List


class Solution:
    def findTheDistanceValue(
        self, arr1: List[int], arr2: List[int], d: int
    ) -> int:
        count = 0
        for i in arr1:
            is_contain = False
            for j in arr2:
                if abs(i - j) <= d:
                    is_contain = True
                    break
            if not is_contain:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6)
    print(answer)
