from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        ret = [0, 1]
        multi = 1
        seq = 0
        for i in range(2, num + 1):
            value = 2 ** multi
            if value > i:
                seq += 1
                ret.append(1 + ret[seq])

            elif value == i:
                multi += 1
                seq = 0
                ret.append(1)
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.countBits(1)
    print(answer)
    "asdasdas"
