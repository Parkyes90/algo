class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = self._combination(characters, combinationLength)
        self.length = len(self.combinations)
        self.index = 0

    def _combination(self, characters, length):
        ret = []
        if length > len(characters):
            return ret
        if length == 1:
            for c in characters:
                ret.append(c)
        elif length > 1:
            for i in range(len(characters) - length + 1):
                for t in self._combination(characters[i + 1 :], length - 1):
                    ret.append(characters[i] + t)
        return ret

    def next(self) -> str:
        value = self.combinations[self.index]
        self.index += 1
        return value

    def hasNext(self) -> bool:
        return self.index < self.length


if __name__ == "__main__":
    obj = CombinationIterator("abc", 2)
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
# Your CombinationIterator object will be instantiated and called as such:

# param_1 = obj.next()
# param_2 = obj.hasNext()
