class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ret = temp = 0
        for s in S:
            if s == "(":
                temp += 1
            else:
                temp -= 1

            if temp == -1:
                ret += 1
                temp = 0
        return ret + temp


if __name__ == "__main__":
    s = Solution()
    answer = s.minAddToMakeValid("()))((")
    print(answer)
