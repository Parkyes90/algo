from typing import List, Union

"""arr: List[int] -> 오름 차순으로 정렬되있다고 가정한다."""


def binary_search(arr: List[int], target: int) -> Union[int, None]:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return None


def recursive_binary_search(
    arr: List[int], target: int, left: int, right: int
):
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid

    if left >= right:
        return None

    if arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)

    return recursive_binary_search(arr, target, left, mid - 1)


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 6, 7, 10]
    test_target = 7
    for_index = binary_search(test_arr, test_target)
    rec_index = recursive_binary_search(
        test_arr, test_target, 0, len(test_arr) - 1
    )
    assert for_index == rec_index
