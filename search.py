from typing import Optional

def binary_interpolation_search(search_value: int, search_collection: list) -> Optional[int]:
    if not search_collection:
        return None

    start = 0
    end = len(search_collection) - 1
    while start <= end:
        pos = start + \
              ((search_value - search_collection[start])//(search_collection[end] - search_collection[start])) * \
              (end - start)

        if pos < start:
            pos = start
        elif pos > end:
            pos = end

        pos_number = search_collection[pos]
        if pos_number == search_value:
            return pos
        elif pos_number < search_value:
            start = pos + 1
        else:
            end = pos - 1

    return None

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
