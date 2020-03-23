from typing import List, Union


def quick_selection(arr: List[int], target: int) -> Union[int, None]:
    """선형 시간을 갖는 선택 알고리즘"""
    if len(arr) - 1 < target:
        return None

    pivot = arr[(len(arr) - 1) // 2]

    return arr[target]


if __name__ == "__main__":
    test_arr = [1, 2, 3, 10, 5, 7, 3, 4]
    test_target = 4
    print(quick_selection(test_arr, test_target))
    assert quick_selection(test_arr, test_target) == 10
