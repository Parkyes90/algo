class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        node = head
        ret = []
        while node:
            ret.append(node.val)
            node = node.next
        return ret == ret[::-1]


if __name__ == "__main__":
    h = ListNode(-129)
    h.next = ListNode(-129)
    s = Solution()
    answer = s.isPalindrome(h)
    print(answer)
