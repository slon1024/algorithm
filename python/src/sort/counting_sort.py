def counting_sort(in_array):
    if len(in_array) < 2:
        return in_array

    loop_min_to_max = range(min(in_array), max(in_array)+1)
    count={}
    for i in loop_min_to_max:
        count[i] = 0

    for i in in_array:
        count[i] += 1

    k = 0
    for i in loop_min_to_max:
        while count[i]  > 0:
            in_array[k] = i
            k += 1
            count[i] -= 1
    return in_array