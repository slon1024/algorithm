
def selection_sort(in_array):
    for i in range(0, len(in_array)):
        min=in_array[i]
        j = i + 1
        while j < len(in_array):
            if in_array[j] < min:
                min=in_array[j]
                in_array[j] = in_array[i]
                in_array[i] = min
            j += 1
    return in_array


    

