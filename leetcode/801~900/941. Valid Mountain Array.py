from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)
        if length < 3:
            return False
        is_up = True
        is_change = False
        for i in range(1, length):
            if A[i] == A[i - 1]:
                return False
            if i > 1 and is_up:
                is_change = True
            if is_up:
                if A[i - 1] > A[i]:
                    is_up = False
            else:
                if A[i - 1] < A[i]:
                    return False
        if is_up:
            return False
        if not is_change:
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.validMountainArray([1, 2, 3, 2])
    print(answer)
