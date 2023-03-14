class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half_index = len(s) // 2
        left, right = s[:half_index], s[half_index:]

        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        vowels_count = 0

        for letter in left:
            if letter in vowels:
                vowels_count += 1
        for letter in right:
            if letter in vowels:
                vowels_count -= 1
        return vowels_count == 0


if __name__ == "__main__":
    s = Solution()
    assert s.halvesAreAlike("book") is True
    assert s.halvesAreAlike("textbook") is False
