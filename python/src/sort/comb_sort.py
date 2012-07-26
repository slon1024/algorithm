
def comb_sort(in_array):
    gap=len(in_array)
    while gap > 1:
        gap = get_gap(gap)
        i=0
        while i+gap < len(in_array):
            if in_array[i+gap] < in_array[i]:
                in_array[i+gap], in_array[i] = in_array[i], in_array[i+gap]
            i += 1
    return in_array


def get_gap(gap):
    return int(gap * 10/11)





