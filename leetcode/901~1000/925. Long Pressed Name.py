class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        if len(name) > len(typed):
            return False
        typed_index = 0
        name_index = 0

        while name_index < len(name):
            name_letter_count = 1
            for j in range(name_index + 1, len(name)):
                if name[name_index] == name[j]:
                    name_index = j
                    name_letter_count += 1
                else:
                    break

            typed_letter_count = 0
            for j in range(typed_index, len(typed)):
                if name[name_index] == typed[j]:
                    typed_index = j
                    typed_letter_count += 1
                else:
                    typed_index += 1
                    break
            if typed_letter_count < name_letter_count:
                return False
            name_index += 1
        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.isLongPressedName("laiden", "laiden")
    print(answer)
