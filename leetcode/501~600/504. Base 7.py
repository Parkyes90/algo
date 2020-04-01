class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        ret = []
        sign = ""
        if num < 0:
            num = -num
            sign = "-"
        while num:
            num, remain = divmod(num, 7)
            ret.append(str(remain))
        return sign + "".join(ret[::-1])


if __name__ == "__main__":
    s = Solution()
    answer = s.convertToBase7(0)
    print(answer)
