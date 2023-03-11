class Solution:
    def minPartitions(self, n: str) -> int:
        answer = 0
        for num in n:
            answer = max(answer, int(num))
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.minPartitions("32") == 3
    assert s.minPartitions("82734") == 8
    assert s.minPartitions("27346209830709182346") == 9
