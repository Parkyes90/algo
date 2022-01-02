from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(sentence.split(" ")) for sentence in sentences])


if __name__ == "__main__":
    s = Solution()
    ans = s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
    print(ans)
