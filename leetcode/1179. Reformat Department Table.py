class Solution:
    def maximum69Number(self, num: int) -> int:
        listed = list(str(num))
        for i in range(len(listed)):
            if listed[i] == "6":
                listed[i] = "9"
                break
        return int("".join(listed))


if __name__ == "__main__":
    s = Solution()
    print(s.maximum69Number(9996))
