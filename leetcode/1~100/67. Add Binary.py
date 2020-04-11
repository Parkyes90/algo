class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b[::-1], a[::-1]
        else:
            a, b = a[::-1], b[::-1]
        index = 0
        ans = ""
        up = 0
        while index < len(a):
            if len(b) <= index:
                up, remain = divmod(int(a[index]) + up, 2)
                ans += str(remain)
            else:
                up, remain = divmod(int(a[index]) + int(b[index]) + up, 2)
                ans += str(remain)
            index += 1
        if up:
            ans += "1"

        return ans[::-1]


if __name__ == "__main__":
    s = Solution()
    answer = s.addBinary("1", "1")
    print(answer)
