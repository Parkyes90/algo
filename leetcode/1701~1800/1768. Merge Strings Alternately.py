from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        for l1, l2 in zip_longest(word1, word2, fillvalue=""):
            answer += f"{l1}{l2}"

        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.mergeAlternately("abc", "pqr") == "apbqcr"
    assert s.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert s.mergeAlternately("abcd", "pq") == "apbqcd"
