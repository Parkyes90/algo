class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        x, y = a.split("+")
        w, v = b.split("+")

        y = int(y[:-1])
        v = int(v[:-1])
        x = int(x)
        w = int(w)

        return f"{x*w-y*v}+{x*v+y*w}i"


if __name__ == "__main__":
    s = Solution()
    answer = s.complexNumberMultiply("78+-76i", "-86+72i")
    print(answer)
