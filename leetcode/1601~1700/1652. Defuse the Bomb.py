from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        ret = []

        for i in range(n):
            el = 0
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    idx = j if j < n else j - n
                    el += code[idx]
            else:
                for j in range(1, abs(k) + 1):
                    idx = i - j
                    idx = idx if idx > -1 else n + idx
                    print(idx)
                    el += code[idx]
            ret.append(el)
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.decrypt([1, 2, 3, 4], 0)
    print(answer)
