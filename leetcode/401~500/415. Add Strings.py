class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = []
        listed_num1 = list(num1)
        listed_num2 = list(num2)
        upper = 0
        while listed_num1 or listed_num2 or upper > 0:
            n1 = 0
            n2 = 0
            if listed_num1:
                n1 = int(listed_num1.pop())
            if listed_num2:
                n2 = int(listed_num2.pop())
            value, remain = divmod(n1 + n2 + upper, 10)
            upper = value
            ret.append(str(remain))
        ret.reverse()
        return "".join(ret)


if __name__ == "__main__":
    s = Solution()
    answer = s.addStrings("1", "9")
    print(answer)
