
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
    i,j = 0,0
    len_i, len_j = len(left), len(right)
    
    while i < len_i and j < len_j:
        if left[i] < right[j]:
            result += [ left[i] ]
            i += 1
        else:
            result += [ right[j] ]
            j += 1

    return result + left[i:] + right[j:]

