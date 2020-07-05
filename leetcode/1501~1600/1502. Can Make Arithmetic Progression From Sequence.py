from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        initial = arr[1] - arr[0]
        for i in range(2, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff != initial:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.canMakeArithmeticProgression([3, 5, 1])
    print(answer)
