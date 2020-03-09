from typing import List


class Solution:
    """
    https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
    """

    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        cache = [max(arr[1:])]

        for i in range(1, len(arr)):
            if i != len(arr) - 1:
                if cache[i - 1] != arr[i]:
                    cache.append(cache[i - 1])
                else:
                    cache.append(max(arr[i + 1 :]))
            else:
                cache.append(-1)
        return cache


if __name__ == "__main__":
    s = Solution()
    answer = s.replaceElements([400])
    print(answer)
