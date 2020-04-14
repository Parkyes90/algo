from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for digit in digits:
            num += str(digit)
        num = int(num) + 1
        ret = []
        for n in str(num):
            ret.append(int(n))
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.plusOne([1, 2, 3])
    print(answer)
