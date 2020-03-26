from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = []
        subtract = 0
        for i in range(n - 1):
            ret.append(i)
            subtract -= i
        ret.append(subtract)
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.sumZero(5)
    print(answer)
