class Solution:
    def checkString(self, s: str) -> bool:
        last_a_index = -1
        first_b_index = -1

        for index, letter in enumerate(s):
            if letter == "a":
                last_a_index = index

        if last_a_index == -1:
            return True

        for index, letter in enumerate(s):
            if letter == "b":
                first_b_index = index
                break

        if first_b_index == -1:
            return True

        return last_a_index < first_b_index


if __name__ == "__main__":
    assert Solution().checkString("aaabbb") is True
    assert Solution().checkString("abab") is False
    assert Solution().checkString("bbb") is True
