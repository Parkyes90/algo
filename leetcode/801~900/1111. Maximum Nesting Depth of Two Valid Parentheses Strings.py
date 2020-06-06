from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ret = []
        temp = 0
        for i, c in enumerate(seq[:-1]):
            if c == seq[i + 1]:
                ret.append(temp)
                temp ^= 1
            else:
                ret.append(temp)
        return ret + [temp]


if __name__ == "__main__":
    s = Solution()
    answer = s.maxDepthAfterSplit("((()))")
    print(answer)
