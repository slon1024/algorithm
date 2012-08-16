def heap_sort(in_array):
    if len(in_array) < 2:
        return in_array;

    length=len(in_array)
    start = (length-2) >> 1
    end = length-1

    while start > -1:
        shift_down(in_array, start, end)
        start -= 1

    while end > 0:
        if in_array[end] < in_array[0]:
            in_array[0], in_array[end] = in_array[end], in_array[0]
        end -= 1
        shift_down(in_array, 0, end)
    return in_array


def shift_down(in_array, start, end):
    root = start
    while root*2 + 1 <= end:
        child = root*2+1
        swap = root

        if in_array[swap] < in_array[child]:
            swap = child

        if child+1 <= end and in_array[swap] < in_array[child+1]:
            swap = child + 1

        if swap != root:
            in_array[swap], in_array[root] = in_array[root], in_array[swap]
            root = swap
        else:
            break


