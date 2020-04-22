from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sub_words = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    sub_words.add(words[i])
        return list(sub_words)


if __name__ == "__main__":
    s = Solution()
    answer = s.stringMatching(["blue", "green", "bu"])
    print(answer)
