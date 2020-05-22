class Solution:
    def minSteps(self, s: str, t: str) -> int:
        letter_count_map = {}
        for le in s:
            letter_count_map[le] = letter_count_map.get(le, 0) + 1
        for le in t:
            if le in letter_count_map and letter_count_map[le] > 0:
                letter_count_map[le] -= 1

        return sum(letter_count_map.values())


if __name__ == "__main__":
    s = Solution()
    answer = s.minSteps("friend", "family")
    print(answer)
