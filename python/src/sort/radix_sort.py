from math import log, ceil

def radix_sort(in_array, base=64):
    if min(in_array) < 0:
        raise Exception('Algorithm expected only positive number')

    for i in range(int( ceil(log(max(in_array), base)) )):

        digits = [ [] for x in range(base) ]
        for num in in_array:
            digits[(num // base ** i) % base] += [num]

        tmp_list = []
        for j in digits:
            tmp_list[len(tmp_list):] = j
        in_array = tmp_list

    return in_array