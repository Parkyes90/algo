class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = 0
        after_s = ""
        for i in range(len(S) - 1, -1, -1):
            if S[i] == "#":
                s_stack += 1
            else:
                if s_stack == 0:
                    after_s += S[i]
                else:
                    s_stack -= 1

        t_stack = 0
        after_t = ""
        for i in range(len(T) - 1, -1, -1):
            if T[i] == "#":
                t_stack += 1
            else:
                if t_stack == 0:
                    after_t += T[i]
                else:
                    t_stack -= 1
        return after_t == after_s


if __name__ == "__main__":
    s = Solution()
    answer = s.backspaceCompare("a#c", "b")
    print(answer)
