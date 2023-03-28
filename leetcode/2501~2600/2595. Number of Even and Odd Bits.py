from typing import List


class Solution:

    def to_binary(self, n: int):
        bits = []
        while n > 0:
            n, remain = divmod(n, 2)
            bits.append(str(remain))

        return "".join(bits)

    def evenOddBit(self, n: int) -> List[int]:
        binary = self.to_binary(n)
        even = 0
        odd = 0
        for index, bit in enumerate(binary):
            if bit == "1":
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]


if __name__ == "__main__":
    assert Solution().evenOddBit(17) == [2, 0]
    assert Solution().evenOddBit(2) == [0, 1]
