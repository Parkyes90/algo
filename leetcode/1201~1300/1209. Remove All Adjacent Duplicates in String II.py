class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for item in s:
            if stack and item == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([item, 1])

        return "".join([item[0] * item[1] for item in stack])


if __name__ == "__main__":
    s = Solution()
    assert s.removeDuplicates("abcd", 2) == "abcd"
    assert s.removeDuplicates("deeedbbcccbdaa", 3) == "aa"
