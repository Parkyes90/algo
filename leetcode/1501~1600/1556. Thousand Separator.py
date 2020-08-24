class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ""
        for idx, number in enumerate(str(n)[::-1], 1):
            ans += number
            if idx % 3 == 0 and idx != len(str(n)):
                ans += "."

        return ans[::-1]


if __name__ == "__main__":
    s = Solution()
    answer = s.thousandSeparator(0)
    print(answer)
