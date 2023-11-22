from typing import Optional

def binary_search(search_value: int, search_collection: list) -> Optional[int]:
    if not search_collection:
        return None

    start = 0
    end = len(search_collection) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_number = search_collection[mid]
        if mid_number == search_value:
            return mid
        elif mid_number < search_value:
            start = mid + 1
        else:
            end = mid - 1

    return None
