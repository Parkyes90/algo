# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        exists = {head.val}
        node = head
        while node.next:
            if node.next.val in exists:
                node.next = node.next.next
                continue
            exists.add(node.next.val)
            node = node.next
        return head


def create_list_node(arr: List[int]):
    arr.reverse()
    h = ListNode(arr.pop())
    node = h
    while arr:
        node.next = ListNode(arr.pop())
        node = node.next
    return h


if __name__ == "__main__":
    s = Solution()
    head = create_list_node([1, 1, 2])
    answer = s.deleteDuplicates(head)
    print(answer)
