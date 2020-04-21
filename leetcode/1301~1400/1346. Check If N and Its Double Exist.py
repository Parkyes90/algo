from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        length = len(arr)
        for i in range(length):
            current = arr[i]
            for j in range(length):
                if j != i and arr[j] * 2 == current:
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    answer = s.checkIfExist([7, 1, 14, 11])
    print(answer)
