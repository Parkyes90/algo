class Solution:
    def reverseBits(self, n: int) -> int:
        ret = []
        while n:
            n, remain = divmod(n, 2)
            ret.append(remain)
        while len(ret) < 32:
            ret.append(0)
        ret = ret[::-1]
        ans = 0
        while ret:
            ans += ret.pop() * 2 ** len(ret)
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.reverseBits(0b00000010100101000001111010011100)
    print(answer)
