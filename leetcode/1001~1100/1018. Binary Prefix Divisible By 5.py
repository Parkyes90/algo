from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ret = [A[0]]
        for i in range(1, len(A)):
            ret.append((ret[i - 1] * 2) + A[i])
        return list(map(lambda x: x % 5 == 0, ret))


if __name__ == "__main__":
    s = Solution()
    answer = s.prefixesDivBy5([1, 1, 0, 0, 0, 1, 0, 0, 1])
    print(answer)
