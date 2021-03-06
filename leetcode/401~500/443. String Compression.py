from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        current = chars[0]
        count = 1
        index = 1
        while index < len(chars):
            if current == chars[index]:
                count += 1
                del chars[index]
                index -= 1
            else:
                str_count = str(count)
                if count > 1:
                    for i in range(len(str_count)):
                        chars.insert(index, str_count[i])
                        index += 1
                count = 1
                current = chars[index]
            if index == len(chars) - 1:
                str_count = str(count)
                if count > 1:
                    for i in str_count:
                        chars.append(i)
                index += len(str_count)
            index += 1
        return len(chars)


if __name__ == "__main__":
    s = Solution()
    answer = s.compress(
        [
            "b",
            "l",
            "l",
            "l",
            "l",
            "l",
            "l",
            "4",
            "4",
            "W",
            "W",
            "&",
            "d",
            "d",
            "d",
            "@",
            "D",
            "D",
            ".",
            ".",
            ".",
            "8",
            "8",
            "8",
            "U",
            "V",
            ">",
            "J",
            "J",
            "k",
            "H",
            "H",
            "=",
            "l",
            "[",
            "[",
            "[",
            "[",
            "[",
            "[",
            "[",
            "a",
            "a",
            "'",
            "<",
            "[",
            "[",
            "y",
            "V",
            "l",
            "l",
            "'",
            "$",
            "E",
            "`",
            "v",
            "k",
            "E",
            "E",
            "t",
            "t",
            "t",
            "t",
            "t",
            "=",
            "=",
            "0",
            "C",
            "a",
            "l",
            "l",
            "l",
            "r",
            "R",
            "M",
            "M",
            "c",
            "c",
            "c",
            "A",
            "A",
            "S",
            "9",
            "9",
            "9",
            "9",
            ")",
            ")",
            "\\",
            "s",
            "\\",
            "\\",
            "y",
            "W",
            "W",
            "W",
            "J",
            "J",
            "J",
            "J",
            "6",
            "6",
            "<",
            "<",
            "E",
            "u",
            "e",
            "e",
            "e",
            "e",
            "e",
            "e",
            "e",
            "e",
            "e",
            "9",
            "9",
            "9",
            "9",
            "R",
            "8",
            "?",
            "F",
            "3",
            "&",
            "&",
            "&",
            "&",
            "f",
            "%",
            "%",
            "2",
            "2",
            "2",
            ")",
            ")",
            ")",
            "J",
            "p",
            "|",
            "D",
            "D",
            "D",
            "s",
            "t",
            "V",
            "V",
            "?",
            "^",
            "^",
            "S",
            "3",
            "3",
            "3",
            "3",
            "h",
            "*",
            "|",
            "|",
            "b",
            "b",
            "a",
            "a",
            "a",
            "r",
            "r",
            "r",
            "r",
            "J",
            ".",
            "^",
            "^",
            "~",
            "g",
            ":",
            ":",
            ":",
            "(",
            "4",
            "4",
            "4",
            "4",
            "w",
            "w",
            "w",
            "w",
            "w",
            "w",
            "w",
            "C",
            "?",
            "=",
            "d",
            "L",
            ":",
            "0",
            "0",
            "c",
            "w",
            "w",
            "w",
            "w",
            "w",
            "w",
            "{",
            "{",
            "t",
            "k",
            "k",
            "k",
            "&",
            "&",
            "&",
            "h",
            "j",
            "j",
            "j",
            "0",
            "3",
            "l",
            ";",
            ";",
            ";",
            ";",
            ";",
            ".",
            ".",
            ".",
            "%",
            "1",
            "1",
            "1",
            "l",
            "9",
            "?",
            "?",
            "?",
            "t",
            ">",
            "E",
            "N",
            "N",
            "@",
            ">",
            ".",
            ".",
            "I",
            "a",
            "a",
            "a",
            "a",
            "B",
            "7",
            "7",
            "{",
            "o",
            "o",
            "-",
            "+",
            "+",
            "+",
            "+",
            "o",
            "o",
            "}",
            "B",
            "B",
            "r",
            "r",
            "r",
            "q",
            "4",
            "4",
            "4",
            "9",
            "W",
            "W",
            "W",
            "W",
            "W",
            "'",
            "'",
            "'",
            "g",
            "J",
            "(",
            "(",
            "(",
            "(",
            "t",
            "t",
            "?",
            ";",
            "g",
            "g",
            "g",
            "0",
            "]",
            "]",
            "]",
        ]
    )
    print(answer)
