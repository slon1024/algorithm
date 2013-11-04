
def bubble_sort(in_array):
    length = len(in_array)
    for i in range(length-1):
        for j in range(i+1, length):
            if in_array[j] < in_array[i]:
                in_array[i], in_array[j] = in_array[j], in_array[i]
    return in_array
