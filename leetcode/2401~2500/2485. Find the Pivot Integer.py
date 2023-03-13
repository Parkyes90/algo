class Solution:
    def pivotInteger(self, n: int) -> int:
        total = sum([i for i in range(1, n + 1)])
        left_sum = 0

        for i in range(1, n + 1):
            if left_sum == total - left_sum - i:
                return i
            left_sum += i
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.pivotInteger(1) == 1
    assert s.pivotInteger(8) == 6
    assert s.pivotInteger(4) == -1
