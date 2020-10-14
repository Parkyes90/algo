class Solution:
    def maxDepth(self, s: str) -> int:
        maximum = 0
        current = 0
        for el in s:
            if el == "(":
                current += 1
            maximum = max(maximum, current)
            if el == ")":
                current -= 1
        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.maxDepth("1")
    print(answer)
