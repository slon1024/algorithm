
def reverse_inserion_sort(in_array):
    for i in range(1, len(in_array)):
        curr_value = in_array[i]
        j = i - 1
        while j > -1 and in_array[j] < curr_value:
            in_array[j+1] = in_array[j]
            j -= 1
        in_array[j+1] = curr_value
    return in_array




