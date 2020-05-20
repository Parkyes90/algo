class Solution:
    def maxPower(self, s: str) -> int:
        letter = s[0]
        power_of_string = 1
        temp = 1
        for i in range(1, len(s)):
            if letter == s[i]:
                temp += 1
            else:
                temp = 1
                letter = s[i]
            if temp > power_of_string:
                power_of_string = temp
        return power_of_string


if __name__ == "__main__":
    s = Solution()
    answer = s.maxPower("touristt")
    print(answer)
