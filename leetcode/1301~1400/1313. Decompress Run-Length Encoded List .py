from typing import List


class Solution:
    """https://leetcode.com/problems/decompress-run-length-encoded-list/"""

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            ret += [val] * freq
        return ret


if __name__ == "__main__":
    s = Solution()
    result = s.decompressRLElist([1, 2, 3, 4])
    print(result)
