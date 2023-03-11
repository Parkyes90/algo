class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for s in S:
            if not stack or s != stack[-1]:
                stack.append(s)
            else:
                stack.pop(-1)
        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.removeDuplicates("abbaca") == "ca"
    assert s.removeDuplicates("azxxzy") == "ay"
