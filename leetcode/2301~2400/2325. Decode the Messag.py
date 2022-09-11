from collections import OrderedDict


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_map = OrderedDict()
        start = ord("a")
        for letter in key:
            if letter in key_map or letter == " ":
                continue
            key_map[letter] = chr(start)
            start += 1

        output = ""
        for letter in message:
            if letter == " ":
                output += " "
            else:
                output += key_map[letter]
        return output
