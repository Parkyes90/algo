# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/"""

    def getDecimalValue(self, head: ListNode) -> int:
        binaries = []
        total = 0
        ref = head
        while ref:
            binaries.append(ref.val)
            ref = ref.next
        binaries.reverse()
        while binaries:
            binary = binaries.pop()
            exp = len(binaries)
            total += binary * 2 ** exp
        return total


def get_head(arr: List[int]):
    arr.reverse()
    h = ListNode(arr.pop())
    ref = h
    while arr:
        ref.next = ListNode(arr.pop())
        ref = ref.next
    return h


if __name__ == "__main__":
    s = Solution()
    head = get_head([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])
    print(s.getDecimalValue(head))
