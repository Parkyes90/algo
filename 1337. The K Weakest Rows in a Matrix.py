from typing import List


class Solution:
    """https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/"""

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = len(mat)
        ret = []
        for row in range(rows):
            ret.append((mat[row].count(1), row))

        ret.sort(key=lambda x: (x[0], x[1]))
        return list(map(lambda x: x[1], ret))[:k]


if __name__ == "__main__":
    s = Solution()
    answer = s.kWeakestRows(
        [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2
    )
    print(answer)
