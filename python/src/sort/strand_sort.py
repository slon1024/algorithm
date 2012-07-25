

def strand_sort( in_array ):
    result=[]
    while len(in_array):
        sublist = loop([in_array.pop(0)], in_array)
        result  = merge(result,sublist)
    
    return result

def loop(sublist, in_array):
    i=0
    while i < len(in_array):
        if in_array[i] > sublist[-1]:
            sublist += [ in_array.pop(i) ]
        else:
            i += 1
    return sublist
        
    
def merge(left, right):
    result = []
    while len(left) and len(right):
        if left[0] < right[0]:
            result += [left.pop(0)]
        else:
            result += [right.pop(0)]
    return result + left + right



