from typing import List, Union


class Solution:
    """https://leetcode.com/problems/increasing-decreasing-string/"""

    def sortString(self, s: str) -> str:
        listed_s: List[Union[str, None]] = list(s)
        listed_s.sort()
        ans = ""

        while listed_s:
            smalls = []
            larges = []
            smalls.append(listed_s[0])
            listed_s[0] = None
            for i in range(1, len(listed_s)):
                if smalls[-1] < listed_s[i]:
                    smalls.append(listed_s[i])
                    listed_s[i] = None
            listed_s = [letter for letter in listed_s if letter is not None]
            length = len(listed_s)

            if length > 0:
                larges.append(listed_s[length - 1])
                listed_s[length - 1] = None
                for i in range(length - 2, -1, -1):
                    if larges[-1] > listed_s[i]:
                        larges.append(listed_s[i])
                        listed_s[i] = None
                listed_s = [
                    letter for letter in listed_s if letter is not None
                ]
            ans += "".join(smalls + larges)
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.sortString("spo")
