class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        first_index = word.find(ch)
        if first_index < 0:
            return word
        return word[: first_index + 1][::-1] + word[first_index + 1 :]


if __name__ == "__main__":
    s = Solution()
    assert s.reversePrefix("abcdefd", "d") == "dcbaefd"
    assert s.reversePrefix("xyxzxe", "z") == "zxyxxe"
    assert s.reversePrefix("abcd", "z") == "abcd"
