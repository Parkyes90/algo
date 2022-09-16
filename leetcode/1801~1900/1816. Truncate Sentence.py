class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        split_s = s.split(" ")
        return " ".join(split_s[:k])


if __name__ == "__main__":
    s = Solution()
    answer = s.truncateSentence("Hello how are you Contestant", 4)
    assert "Hello how are you" == answer
