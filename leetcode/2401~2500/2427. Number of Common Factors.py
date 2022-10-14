class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        min_val = min(a, b)
        count = 0
        for i in range(1, min_val + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.commonFactors(12, 6)
    assert 4 == answer
