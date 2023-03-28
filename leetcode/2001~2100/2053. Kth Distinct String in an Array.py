from collections import OrderedDict
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ordered_dict = OrderedDict()
        order = 0
        for item in arr:
            if item not in ordered_dict:
                ordered_dict[item] = 0
            ordered_dict[item] += 1
        for item, frequency in ordered_dict.items():
            if frequency == 1:
                order += 1
                if order == k:
                    return item
        return ""


if __name__ == "__main__":
    assert Solution().kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a"
    assert Solution().kthDistinct(["aaa", "aa", "a"], 1) == "aaa"
