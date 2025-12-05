from typing import List, Tuple, Optional


def binary_search_upper_bound(
        arr: List[float], target: float
) -> Tuple[int, Optional[float]]:
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] >= target:
            upper_bound = arr[mid]
            right = mid - 1

        else:
            left = mid + 1
    return iterations, upper_bound


if __name__ == "__main__":
    arr = [1.5, 2.3, 3.7, 4.0, 5.6, 6.1]
    print(binary_search_upper_bound(arr, 4.5))  # (3, 5.6)
    print(binary_search_upper_bound(arr, 6.5))  # (3, None)
    print(binary_search_upper_bound(arr, 0.5))  # (3, 1.5)
    print(binary_search_upper_bound(arr, 3.7))  # (3, 4.0)

