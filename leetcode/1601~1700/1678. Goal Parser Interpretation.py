class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        parsing_map = {"G": "G", "()": "o", "(al)": "al"}
        index = 0
        while index < len(command):
            for offset in [1, 2, 4]:
                partial_command = command[index : index + offset]
                if parsing_map.get(partial_command):
                    ans += parsing_map[partial_command]
                    index += offset
                    break
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.interpret("G()()()()(al)")
    assert answer == "Gooooal"
