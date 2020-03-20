class Solution:
    """https://leetcode.com/problems/is-subsequence/"""

    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        s_idx = 0
        while idx < len(t) and s_idx < len(s):
            if t[idx] == s[s_idx]:
                s_idx += 1
            idx += 1

        return s_idx == len(s)


if __name__ == "__main__":
    s = Solution()
    answer = s.isSubsequence("axc", "ahbgdc")
    print(answer)
