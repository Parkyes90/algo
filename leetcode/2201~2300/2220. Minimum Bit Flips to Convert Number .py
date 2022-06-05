class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_start = self.remove_prefix(bin(start))
        bin_goal = self.remove_prefix(bin(goal))

        bin_start_length = len(bin_start)
        bin_goal_length = len(bin_goal)

        if bin_start_length < bin_goal_length:
            bin_start = f"{'0' * (bin_goal_length - bin_start_length)}{bin_start}"
        elif bin_goal_length < bin_start_length:
            bin_goal = f"{'0' * (bin_start_length - bin_goal_length)}{bin_goal}"

        result = 0
        for start_bit, goal_bit in zip(bin_start, bin_goal):
            if start_bit != goal_bit:
                result += 1

        return result

    def remove_prefix(self, binary: str):
        return binary[2:]


if __name__ == "__main__":
    s = Solution()
    assert s.minBitFlips(10, 7) == 3
