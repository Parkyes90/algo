class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        guess_map = {}
        secret_map = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                guess_map[guess[i]] = guess_map.get(guess[i], 0) + 1
                secret_map[secret[i]] = secret_map.get(secret[i], 0) + 1
        for key in guess_map:
            if key in secret_map:
                cows += min(guess_map[key], secret_map[key])

        return f"{bulls}A{cows}B"


if __name__ == "__main__":
    s = Solution()
    answer = s.getHint("1123", "2211")
    print(answer)
