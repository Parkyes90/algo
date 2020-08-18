from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12])
    print(answer)
