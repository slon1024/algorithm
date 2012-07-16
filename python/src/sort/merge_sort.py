
def merge_sort(in_array):
    length = len(in_array)
    if length < 2:
        return in_array

    middle = length / 2
    left   = merge_sort( in_array[:middle] )
    right  = merge_sort( in_array[middle:])
    return merge( left, right )


def merge(left, right):
    result = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result += [ left[i] ]
            i += 1
        else:
            result += [ right[j] ]
            j += 1

    result += left[i:]
    result += right[j:]
    return result


