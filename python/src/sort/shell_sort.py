
def shell_sort(in_array):
    gap=len(in_array)
    while gap > 1:
        gap = get_gap(gap)
        i=gap
        while i < len(in_array):
            curr_value = in_array[i]
            j = i - gap
            while j > -1 and in_array[j] > curr_value:
                in_array[j+gap] = in_array[j]
                j -= gap
            in_array[j+gap] = curr_value
            i += gap 
    return in_array


def get_gap(gap):
    return int(gap * 10/11)






