
def merge_sort(in_array):
    length = len(in_array)
    if length < 2:
        return in_array

    middle = length >> 1
    left   = merge_sort( in_array[:middle] )
    right  = merge_sort( in_array[middle:])
    return merge( left, right )


def merge(left, right):
    result = []
    while len(left) and len(right):
        if left[0] < right[0]:
            result += [left.pop(0)]
        else:
            result += [right.pop(0)]
    return result + left + right

