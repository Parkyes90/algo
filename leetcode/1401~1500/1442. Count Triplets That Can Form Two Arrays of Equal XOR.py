from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        dp = {0: [-1]}
        xor = 0
        answer = 0
        for i in range(len(arr)):
            xor ^= arr[i]
            if xor not in dp:
                dp[xor] = []
            for j in dp[xor]:
                answer += max(0, i - j - 1)
            dp[xor].append(i)

        return answer


if __name__ == "__main__":
    s = Solution()
    ans = s.countTriplets([1, 1, 1, 1, 1])
    print(ans)
