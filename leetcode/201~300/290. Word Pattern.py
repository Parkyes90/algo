class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        count_map = {}
        listed = str.split()
        if len(pattern) != len(listed):
            return False
        for k, v in zip(pattern, listed):
            if k in count_map:
                if count_map[k] != v:
                    return False
            else:
                count_map[k] = v
        ret = set()
        for k in count_map.keys():
            if count_map[k] in ret:
                return False
            ret.add(count_map[k])
        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.wordPattern("abba", "dog dog dog dog")
    print(answer)
