class Solution:
    def reformat(self, s: str) -> str:
        count_map = {"letters": 0, "digits": 0}
        letters = []
        digits = []
        for element in s:
            if element.isdigit():
                count_map["digits"] += 1
                digits.append(element)
            else:
                count_map["letters"] += 1
                letters.append(element)
        ans = ""
        if abs(count_map["letters"] - count_map["digits"]) > 1:
            return ans
        letters.reverse()
        digits.reverse()

        while letters and digits:
            letter = letters.pop()
            digit = digits.pop()
            if len(letters) > len(digits):
                ans += letter + digit
            else:
                ans += digit + letter
        if letters:
            ans += letters.pop()
        if digits:
            ans += digits.pop()
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.reformat("a0b1c2")
    print(answer)
