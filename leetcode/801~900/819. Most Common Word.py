from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = "!?',;."
        for p in punctuation:
            paragraph = paragraph.replace(p, " ")
        listed = paragraph.split(" ")
        count_map = {}
        banned_set = set(banned)
        for word in listed:
            lower = word.lower()
            if lower in banned_set or lower == "":
                continue
            if lower not in count_map:
                count_map[lower] = 1
            else:
                count_map[lower] += 1
        maximum = max(count_map.values())
        for word, count in count_map.items():
            if count == maximum:
                return word
        return ""


if __name__ == "__main__":
    s = Solution()
    answer = s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])
    print(answer)
