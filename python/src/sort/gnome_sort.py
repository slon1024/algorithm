
def gnome_sort(in_array):
    curr, length = 0, len(in_array)
    nxt = curr + 1    
    while nxt < length:
        if in_array[curr] > in_array[nxt]:
            tmp = in_array[curr]
            in_array[curr] = in_array[nxt]
            in_array[nxt]  = tmp
            
            if curr > 0:
                curr -= 1
        else:
            curr += 1 

        nxt = curr + 1 
    return in_array


