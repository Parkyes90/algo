from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ret = []
        length = len(A)
        temp = sorted(range(1, length + 1), key=lambda x: -A[x - 1])
        for t in temp:
            for r in ret:
                if t <= r:
                    t = r + 1 - t
            ret += [t, length]
            length -= 1
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.pancakeSort([1, 2, 3])
    print(answer)
