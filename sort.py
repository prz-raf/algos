def selection_sort(target_list: list) -> list:
    current_start = 0
    last_element = len(target_list)

    while current_start < last_element - 1:
        min_el_index = current_start

        for i in range(current_start + 1, last_element):
            if target_list[i] < target_list[min_el_index]:
                min_el_index = i

        target_list[current_start], target_list[min_el_index] = target_list[min_el_index], target_list[current_start]
        current_start = current_start + 1
