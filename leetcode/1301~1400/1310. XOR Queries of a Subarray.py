from typing import List


class Solution:
    def xorQueries(
        self, arr: List[int], queries: List[List[int]]
    ) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        ret = []

        for left, right in queries:
            if left == 0:
                ret.append(arr[right])
                continue

            if left == right and right > 0:
                ret.append(arr[right] ^ arr[right - 1])
                continue

            ret.append(arr[left - 1] ^ arr[right])

        return ret


if __name__ == "__main__":
    s = Solution()
    ans = s.xorQueries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]])
    print(ans)
