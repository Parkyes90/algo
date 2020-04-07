class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 2:
            return "1"
        temp = "1"
        for _ in range(n - 1):
            letter = temp[0]
            count = 1
            temp2 = ""
            for i in range(1, len(temp)):
                if letter == temp[i]:
                    count += 1
                else:
                    temp2 += str(count) + letter
                    count = 1
                    letter = temp[i]
            temp2 += str(count) + letter
            temp = temp2
        return temp


if __name__ == "__main__":
    s = Solution()
    answer = s.countAndSay(30)
    print(answer)
