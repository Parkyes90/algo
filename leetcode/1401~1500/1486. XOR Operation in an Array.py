class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ret = start
        for i in range(1, n):
            ret ^= start + 2 * i
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.xorOperation(4, 3)
    print(answer)
