from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1 and y == 1:
            if bound < 2:
                return []
            else:
                return [2]

        ret = set()
        i = 0
        while True:
            j = 0
            outer = x ** i + y ** j
            if outer > bound:
                break
            else:
                ret.add(outer)
            if y != 1:
                while True:
                    inner = x ** i + y ** j
                    if inner > bound:
                        if x == 1:
                            listed = list(ret)
                            listed.sort()
                            return listed
                        break
                    else:
                        ret.add(inner)

                    j += 1
            i += 1
        listed = list(ret)
        listed.sort()
        return listed


if __name__ == "__main__":
    s = Solution()
    answer = s.powerfulIntegers(3, 5, 15)
    print(answer)
