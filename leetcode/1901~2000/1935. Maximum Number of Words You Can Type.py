class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        broken_letters_set = set(brokenLetters)
        for word in text.split(" "):
            is_enable_typing = True
            for letter in word:
                if letter in broken_letters_set:
                    is_enable_typing = False
            if is_enable_typing:
                count += 1
        return count


if __name__ == "__main__":
    assert Solution().canBeTypedWords("hello world", "ad") == 1
    assert Solution().canBeTypedWords("leet code", "lt") == 1
    assert Solution().canBeTypedWords("leet code", "e") == 0
