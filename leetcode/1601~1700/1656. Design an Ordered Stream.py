from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.values = []
        self.cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values.append((idKey, value))

        result = []
        self.values.sort(key=lambda x: x[0])
        del_indexes = []
        for i in range(len(self.values)):
            key = self.values[i][0]
            if key == self.cur:
                self.cur += 1
                result.append(self.values[i][1])
                del_indexes.append(i)
            else:
                break

        for del_index in del_indexes:
            self.values[del_index] = None
        self.values = [v for v in self.values if v is not None]
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
