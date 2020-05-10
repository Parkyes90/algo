from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        maximum = max(target)
        target_set = set(target)
        ret = []
        for i in range(1, maximum + 1):
            if i in target_set:
                ret.append("Push")
            else:
                ret.append("Push")
                ret.append("Pop")
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.buildArray([2, 3, 4], 4)
    print(answer)
