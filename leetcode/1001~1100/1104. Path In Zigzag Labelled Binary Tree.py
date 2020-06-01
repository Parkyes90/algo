from typing import List


class Solution:
    def sum(self, n):
        ans = 0
        for i in range(n):
            ans += 2 ** i
        return ans

    def pathInZigZagTree(self, label: int) -> List[int]:
        ret = []
        n = 1
        while len(ret) <= label:
            temp = []
            for i in range(int(2 ** (n - 1)), 2 ** n):
                temp.append(i)
            if n % 2 == 0:
                temp.reverse()
            ret += temp
            n += 1
        ans = []
        index = ret.index(label)
        while index > -1:
            ans.append(ret[index])
            # left
            if index % 2 != 0:
                index = (index - 1) // 2
            # right
            else:
                index = (index - 2) // 2
        ans.sort()
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.pathInZigZagTree(26)
    print(answer)
