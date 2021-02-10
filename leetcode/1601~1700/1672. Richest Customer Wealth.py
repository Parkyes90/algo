from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for account in accounts:
            sum_account = sum(account)
            if maximum < sum_account:
                maximum = sum_account
        return maximum


if __name__ == "__main__":
    s = Solution()
    answer = s.maximumWealth([[1, 2, 3], [3, 2, 1]])
    assert answer == 6
