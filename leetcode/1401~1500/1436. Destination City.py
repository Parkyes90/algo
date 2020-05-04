from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        _, end = paths[0]
        while True:
            is_exists = False
            for i in range(len(paths)):
                s, e = paths[i]
                if s == end:
                    is_exists = True
                    end = e
                    break
            if not is_exists:
                break
        return end


if __name__ == "__main__":
    s = Solution()
    answer = s.destCity([["A", "Z"]])
    print(answer)
