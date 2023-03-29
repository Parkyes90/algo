from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        nums2_set = set(nums2)
        nums1_set = set(nums1)
        answer.append(list(nums1_set.difference(nums2_set)))
        answer.append(list(nums2_set.difference(nums1_set)))
        return answer


if __name__ == "__main__":
    assert Solution().findDifference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]]
    assert Solution().findDifference([1, 2, 3, 3], [1, 1, 2, 2]) == [[3], []]
