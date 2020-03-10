class Solution:
    def freqAlphabets(self, s: str) -> str:
        """https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/"""
        encode_map = {
            str(i - 96) if i < 97 + 9 else str(i - 96) + "#": chr(i)
            for i in range(97, 97 + 26)
        }
        index = 0
        ans = ""
        while index < len(s):
            triple = s[index : index + 3]
            single = s[index]
            if encode_map.get(triple):
                ans += encode_map[triple]
                index += len(triple)
            else:
                ans += encode_map[single]
                index += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.freqAlphabets(
        "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    )
    print(answer)
