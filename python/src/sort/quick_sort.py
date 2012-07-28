
def quick_sort(in_array):
    if len(in_array) < 2:
        return in_array
    
    pivot=get_pivot(in_array)
    less, greater=[], []

    for i in range(len(in_array)):
        if in_array[i] < pivot:
            less += [in_array[i]]
        else:
            greater += [in_array[i]]
    
    return quick_sort(less) + [pivot] + quick_sort(greater)

def get_pivot(in_array):
    index=len(in_array) >> 1
    return in_array.pop( index )



