class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_length = len(s)
        temp = []
        for i in range(1, s_length):
            if s_length % i == 0:
                temp.append(i)
        for t in temp:
            multi = s_length // t
            for i in range(s_length - t + 1):
                if s[i : t + i] * multi == s:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.repeatedSubstringPattern("a")
    print(answer)
