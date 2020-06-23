from typing import List


class Solution:
    def intervalIntersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:
        ret = []
        i = j = 0
        while i < len(A) and j < len(B):
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            if low <= high:
                ret.append([low, high])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]],
    )
    print(answer)
