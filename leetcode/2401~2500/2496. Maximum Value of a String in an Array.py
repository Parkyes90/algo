from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        output = 0
        for letters in strs:
            print(letters)
            if letters.isdigit():
                output = max(int(letters), output)
            else:
                output = max(len(letters), output)
        return output


if __name__ == "__main__":
    s = Solution()
    assert s.maximumValue(["alic3", "bob", "3", "4", "00000"]) == 5
    assert s.maximumValue(["1", "01", "001", "0001"]) == 1
