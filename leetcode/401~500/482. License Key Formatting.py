class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        separate = S.split("-")
        merged = "".join(separate).upper()
        remain = len(merged) % K
        ans = merged[:remain]
        merged = merged[remain:]
        length = 0
        temp = ""
        for s in merged:
            temp += s
            length += 1
            if length == K:
                if not ans:
                    ans += temp
                else:
                    ans += "-" + temp
                length = 0
                temp = ""
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.licenseKeyFormatting("2-5g-3-J", 2)
    print(answer)
