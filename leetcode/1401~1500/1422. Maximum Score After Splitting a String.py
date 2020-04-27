class Solution:
    def maxScore(self, s: str) -> int:
        maximum = 0
        split_index = 1
        length = len(s)
        while split_index < length:
            left = s[:split_index].count("0")
            right = s[split_index:].count("1")
            if left + right > maximum:
                maximum = left + right
            split_index += 1
        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.maxScore("1111")
    print(answer)
