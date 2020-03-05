from typing import List


def partition(arr: List[int], left: int, right: int) -> int:
    pivot = arr[left]
    low = left + 1
    high = right
    while low < high:
        while arr[low] < pivot and low <= right:
            low += 1
        while arr[high] > pivot and high >= left:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[left], arr[high] = arr[high], arr[left]
    return high


def quick_sort(arr: List[int], left: int, right: int) -> None:
    """
    제자리 정렬, stable 하지 않은 정렬 (기존 원본 배열의 순서를 보장할 수 없음.)
    최악 시간 복잡도: n^2
    피벗은 부분 배열의 첫번째 요소로 정함
    """
    if left > right:
        return None
    p = partition(arr, left, right)
    quick_sort(arr, left, p - 1)
    quick_sort(arr, p + 1, right)


if __name__ == "__main__":
    unsorted_arr = [8, 1, 2, 40, 2, 5, 7, 10]
    quick_sort(unsorted_arr, 0, len(unsorted_arr) - 1)
    assert unsorted_arr == sorted(unsorted_arr)
