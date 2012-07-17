
def binary_search(in_array, key):
    start, finish = 0, len(in_array)
    while finish > start:
        middle = start + (finish-start) / 2
        if key == in_array[middle]:
            return middle
        if key < in_array[middle]:
            finish = middle -1
        else:
            start = middle + 1
    return None

