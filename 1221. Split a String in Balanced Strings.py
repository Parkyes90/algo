class Solution:
    """https://leetcode.com/problems/split-a-string-in-balanced-strings/"""

    def balancedStringSplit(self, s: str) -> int:
        count = 0
        letter_map = {"L": 0, "R": 0}
        for el in s:
            letter_map[el] += 1
            if letter_map["L"] == letter_map["R"]:
                letter_map["L"] = letter_map["R"] = 0
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.balancedStringSplit("RLRRRLLRLL"))
