class Solution:
    def convertToTitle(self, n: int) -> str:
        letter_map = {
            index: chr(letter)
            for index, letter in enumerate(range(ord("A"), ord("Z") + 1))
        }
        ret = []
        ans = ""
        while n - 1 > 0:
            n, remain = divmod(n - 1, 26)
            ret.append(remain)

        if n - 1 == 0:
            ret.append(n - 1)
        for i in reversed(ret):
            ans += letter_map[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.convertToTitle(702)
    print(answer)
