
def recursion_insertion_sort(in_array):
    if len(in_array) < 2:
        return in_array

    last   = in_array[-1]
    rest   = recursion_insertion_sort( in_array[:-1] )
    return merge_recursion_insertion_sort( rest, last )

def merge_recursion_insertion_sort( rest, last ):
    for i in range( len(rest) ):
        if rest[i] > last:
            return rest[0:i] + [last] + rest[i:]
    return rest + [last]

