from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_length = 1
        total = 0
        while odd_length <= len(arr):
            for i in range(len(arr) + 1 - odd_length):
                total += sum(arr[i : i + odd_length])
            odd_length += 2
        return total


if __name__ == "__main__":
    s = Solution()
    ans = s.sumOddLengthSubarrays([10, 11, 12])
    print(ans)
