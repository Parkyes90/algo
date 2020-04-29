import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        multiplier = int(math.log2(n) / math.log2(5))
        count = 0
        for i in range(1, multiplier + 1):
            count += n // 5 ** i
        return count

    def trailingZeroes2(self, n: int) -> int:
        ret = 1
        for i in range(1, n + 1):
            ret *= i
        str_ret = str(ret)
        count = 0
        for i in range(len(str_ret) - 1, -1, -1):
            if str_ret[i] == "0":
                count += 1
            else:
                break
        return count


if __name__ == "__main__":
    s = Solution()
    for i in range(0, 201):
        answer = s.trailingZeroes(i)
        answer2 = s.trailingZeroes2(i)
        if answer != answer2:
            print("false", answer, answer2, i)
    # print(answer)
