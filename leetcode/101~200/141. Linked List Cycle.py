# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        visited = set()
        node = head
        while node.next:
            if id(node) in visited:
                return True
            visited.add(id(node))
            node = node.next
        return False


def create_head(arr: List[int]):
    arr = arr[::-1]
    head = ListNode(arr.pop())
    node = head
    while arr:
        node.next = ListNode(arr.pop())
        node = node.next
    return head


if __name__ == "__main__":
    test_arr = [3, 2, 0, -4]
    h = create_head(test_arr)
    h.next.next.next.next = h.next
    s = Solution()
    answer = s.hasCycle(h)
    print(answer)
