# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> ListNode:
        id_set = set()
        a_node = headA
        while a_node:
            id_set.add(id(a_node))
            a_node = a_node.next
        b_node = headB
        while b_node:
            if id(b_node) in id_set:
                return b_node
            b_node = b_node.next
        return None


def create_linked_list(arr: List[int]):
    arr = arr[::-1]
    head = ListNode(arr.pop())
    node = head
    while arr:
        node.next = ListNode(arr.pop())
        node = node.next
    return head


if __name__ == "__main__":
    arr1 = [2, 6, 4]
    arr2 = [1, 5]
    # intersect = create_linked_list([8, 4, 5])
    h1 = create_linked_list(arr1)
    h2 = create_linked_list(arr2)
    # h1.next.next = intersect
    # h2.next.next.next = intersect
    s = Solution()
    answer = s.getIntersectionNode(h1, h2)
    print(answer)
