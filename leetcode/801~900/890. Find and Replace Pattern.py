from typing import List
from collections import OrderedDict


class Solution:
    def findAndReplacePattern(
        self, words: List[str], pattern: str
    ) -> List[str]:
        count_map = OrderedDict()
        for i in range(len(pattern)):
            if pattern[i] not in count_map:
                count_map[pattern[i]] = [i]
            else:
                count_map[pattern[i]].append(i)
        ret = []
        for word in words:
            c_m = OrderedDict()
            for i in range(len(word)):
                if word[i] not in c_m:
                    c_m[word[i]] = [i]
                else:
                    c_m[word[i]].append(i)
            if tuple(count_map.values()) == tuple(c_m.values()):
                ret.append(word)
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.findAndReplacePattern(
        ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"
    )
    print(answer)
