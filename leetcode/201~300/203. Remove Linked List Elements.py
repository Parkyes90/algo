# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        node = head
        nodes = []
        while node:
            if node.val != val:
                nodes.append(node.val)
            node = node.next
        return create_head(nodes)


def create_head(arr):
    if not arr:
        return None
    arr.reverse()
    head = ListNode(arr.pop())
    node = head
    while arr:
        node.next = ListNode(arr.pop())
        node = node.next
    return head


if __name__ == "__main__":
    arr = [1, 2, 6, 3, 4, 5, 6]
    h = create_head(arr)
    s = Solution()
    answer = s.removeElements(h, 6)
    print(answer)
