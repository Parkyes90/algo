class Solution:
    def countSegments(self, s: str) -> int:
        listed = s.split(" ")
        count = 0
        for el in listed:
            if el:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.countSegments("Hello, my name is     John")
    print(answer)
