from math import log, ceil

def radix_sort(in_array, base=64):
    if len(in_array) < 1:
        return in_array

    if min(in_array) < 0:
         raise ValueError('Algorithm expected only positive number')

    max_val = int( ceil(log(max(in_array), base)) )
    for i in range(max_val):
        digits = [ [] for x in range(base) ]
        for num in in_array:
            digits[(num // base ** i) % base] += [num]

        tmp_list = []
        for j in digits:
            tmp_list[len(tmp_list):] = j
        in_array = tmp_list

    return in_array