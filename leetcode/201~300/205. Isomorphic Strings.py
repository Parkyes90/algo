class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_map = {}
        for s_el, t_el in zip(s, t):
            letter_map[s_el] = t_el
        trans = ""
        count_map = {}
        for key, value in letter_map.items():
            if value not in count_map:
                count_map[value] = 1
            else:
                if key != value:
                    return False
        for s_el in s:
            trans += letter_map[s_el]
        return trans == t


if __name__ == "__main__":
    s = Solution()
    answer = s.isIsomorphic("ab", "aa")
    print(answer)
