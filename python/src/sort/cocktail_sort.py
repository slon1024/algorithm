
def cocktail_sort(in_array):
    i, k = 0, len(in_array)-1
    
    while i < k:
        for j in range(i,k+1):
            if in_array[j] < in_array[i]:
                tmp = in_array[i]
                in_array[i] = in_array[j]
                in_array[j] = tmp

        for m in range(k, i, -1):
            if in_array[m] > in_array[k]:
                tmp = in_array[m]
                in_array[m] = in_array[k]
                in_array[k] = tmp

        i += 1
        k -= 1
                
    return in_array



    

