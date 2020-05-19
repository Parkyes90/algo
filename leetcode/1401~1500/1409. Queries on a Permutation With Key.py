from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]
        ret = []
        for query in queries:
            index = p.index(query)
            print(p[index], index, p)
            ret.append(index)
            p.insert(0, p.pop(index))
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.processQueries([7, 5, 5, 8, 3], 8)
    print(answer)
