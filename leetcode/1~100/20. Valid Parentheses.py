class Solution:
    p_map = {"}": "{", "]": "[", ")": "("}
    count_map = {"{": 0, "[": 0, "(": 0}

    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        for s_el in s:
            if s_el not in self.p_map:
                stack.append(s_el)
                self.count_map[s_el] += 1
            elif s_el in self.p_map and (
                len(stack) == 0 or self.count_map[self.p_map[s_el]] <= 0
            ):
                return False
            elif (
                s_el in self.p_map
                and len(stack) > 0
                and self.p_map[s_el] == stack[-1]
            ):
                pop = stack.pop()
                self.count_map[pop] -= 1
        if not stack:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.isValid("{[]}")
    print(answer)
