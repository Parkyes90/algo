from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        x = ""
        for a in A:
            x += str(a)
        ret = []
        for el in str(int(x) + K):
            ret.append(int(el))
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1)
    print(answer)
