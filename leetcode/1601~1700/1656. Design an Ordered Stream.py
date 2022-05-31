from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.values = {}
        self.cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        result = []
        self.values.update({idKey: value})
        while self.cur in self.values:
            result.append(self.values[self.cur])
            self.cur += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

if __name__ == "__main__":
    obj = OrderedStream(5)
    assert obj.insert(3, "ccccc") == []
    assert obj.insert(1, "aaaaa") == ["aaaaa"]
    assert obj.insert(2, "bbbbb") == ["bbbbb", "ccccc"]
    assert obj.insert(5, "eeeee") == []
    assert obj.insert(4, "ddddd") == ["ddddd", "eeeee"]
