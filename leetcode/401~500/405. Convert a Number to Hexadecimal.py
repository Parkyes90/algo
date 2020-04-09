class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = 2 ** 32 + num
        hex_map = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        ret = []

        while num:
            num, remain = divmod(num, 16)
            if remain < 10:
                ret.append(str(remain))
            else:
                ret.append(hex_map[remain])

        return "".join(ret[::-1])


if __name__ == "__main__":
    s = Solution()
    answer = s.toHex(0)
    print(answer)
