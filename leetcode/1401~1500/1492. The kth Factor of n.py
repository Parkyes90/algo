class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ret = []
        for i in range(1, n + 1):
            if n % i == 0:
                ret.append(i)
        try:
            return ret[k - 1]
        except IndexError:
            return -1


if __name__ == "__main__":
    s = Solution()
    answer = s.kthFactor(12, 3)
    print(answer)
