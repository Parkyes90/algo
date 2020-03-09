from typing import List


class Solution:
    """
    https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
    """

    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rmax, result = -1, [0] * len(arr)
        for i in reversed(range(len(arr))):
            result[i], rmax = rmax, max(rmax, arr[i])
        return result


if __name__ == "__main__":
    s = Solution()
    answer = s.replaceElements([400])
    print(answer)
