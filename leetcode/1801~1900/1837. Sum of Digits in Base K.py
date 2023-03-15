class Solution:
    def decimal_to_base(self, n: int, k: int):
        digits = []

        while n > 0:
            n, remainder = divmod(n, k)
            digits.append(str(remainder))
        return "".join(digits[::-1])

    def sumBase(self, n: int, k: int) -> int:
        to_base = self.decimal_to_base(n, k)

        return sum(int(digit) for digit in to_base)


if __name__ == "__main__":
    s = Solution()
    assert s.sumBase(34, 6) == 9
    assert s.sumBase(10, 10) == 1
