from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}

        for i in range(len(S)):
            last[S[i]] = i

        j = i = 0
        ret = []
        for idx, letter in enumerate(S):
            j = max(j, last[letter])
            if idx == j:
                ret.append(idx - i + 1)
                i = idx + 1
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.partitionLabels("ababcbacadefegdehijhklij")
    print(answer)
