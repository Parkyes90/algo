from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        def f(node):
            if node == n - 1:
                return [[n - 1]]
            ret = []
            for j in graph[node]:
                for path in f(j):
                    ret.append([node] + path)
            return ret

        return f(0)


if __name__ == "__main__":
    s = Solution()
    answer = s.allPathsSourceTarget([[1, 2], [3], [3], []])
    print(answer)
