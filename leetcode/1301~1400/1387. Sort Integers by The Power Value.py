class Solution:
    def step(self, x):
        if x % 2 == 0:
            return x / 2
        return 3 * x + 1

    def getKth(self, lo: int, hi: int, k: int) -> int:
        ret = []
        for i in range(lo, hi + 1):
            value = i
            count = 0
            while value != 1:
                count += 1
                value = self.step(value)
            ret.append((i, count))
        ret.sort(key=lambda x: x[1])
        return ret[k - 1][0]


if __name__ == "__main__":
    s = Solution()
    answer = s.getKth(7, 11, 4)
    print(answer)
