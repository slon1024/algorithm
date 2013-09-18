def heap_size(heap):
    """(list) -> int

    Return the number of elements in the heap stored within the array.
    >>>heap_size([])
    0
    >>>heap_size([1,2,3,4,5])
    5
    """
    return len(heap)


def parent(index):
    """(int) -> (int)

    Return the index of parent of node at index i.
    >>>parent(4)
    1
    >>>parent(9)
    4
    """

    return (index -1) >> 1

def left_child(index):
    """(int) -> int

    Return the index of left child of node at index i.
    >>>left(2)
    4
    >>>left(8)
    16
    """

    return index << 1 | 1

def right_child(index):
    """(int) -> int

    Return the index of right child of node at index i.
    >>>right(2)
    5
    >>>right(8)
    9
    """

    return (index << 1) + 2


def max_heapify(heap, index):
    """(list, int) -> NoneType

    This function is responsible for maintaining the heap property of a heap.
    This operates runs at O(lg n).
    >>>heap = [5, 1, 2, 4, 0, 8, 7, 1, 10]
    >>>max_heapify(heap, parent(heap_size(A)))
    >>>heap
    [5, 1, 2, 4, 10, 8, 7, 1, 0]
    """
    size = heap_size(heap)

    while True:
        left_index = left_child(index)
        right_index = right_child(index)
        largest = index

        if left_index < size and heap[left_index] > heap[largest]:
            largest = left_index
        if right_index < size and heap[right_index] > heap[largest]:
            largest = right_index

        if largest == index:
            break

        heap[index], heap[largest] = heap[largest], heap[index]
        index = largest


def rec_max_heapify(heap, index):
    """(list, int) -> NoneType

    This function is responsible for maintaining the heap property of a heap.
    This operates runs at O(lg n).
    This function is recursive.

    >>>heap = [5, 1, 2, 4, 0, 8, 7, 1, 10]
    >>>max_heapify(heap, parent(heap_size(A)))
    >>>heap
    [5, 1, 2, 4, 10, 8, 7, 1, 0]
    """
    size = heap_size(heap)
    left_index = left_child(index)
    right_index = right_child(index)

    largest = index

    if left_index < size and heap[left_index] > heap[largest]:
        largest = left_index
    if right_index < size and heap[right_index] > heap[largest]:
        largest = right_index

    if index != largest:
        heap[index], heap[largest] = heap[largest], heap[index]
        max_heapify(heap, largest)


def build_max_heap(heap):
    """(list) -> NoneType

    This function builds a max-heap from an unordered array.
    This operates runs at O(n).
    >>>heap = [5, 1, 2, 4, 0, 8, 7, 1, 10]
    >>>build_max_heap(heap)
    >>>heap
    [10, 5, 8, 4, 0, 2, 7, 1, 1]
    """
    for index in range(parent(heap_size(heap)-1), -1, -1):
        #You can also use a recursive function: "rec_max_heapify(heap, index)". The result will be identical.
        max_heapify(heap, index)


def max_heap_sort(heap):
    """(list) -> list

    This function is responsible for sorted heap from an unordered array.
    This operates runs at O(n lg n).
    >>>max_heap_sort([5,3,8,2,8,10,46,23])
    [46, 23, 10, 8, 8, 5, 3, 2]
    """
    build_max_heap(heap)
    result=[]

    for index in range(heap_size(heap)-1, -1, -1):
        heap[0], heap[-1] = heap[-1], heap[0]
        result += [heap.pop()]
        max_heapify(heap, 0)

    return result


def max_heap_insert(heap, item):
    """(list, object) -> noneType

    Insert a new item in the heap.
    This operates runs at O(lg n).

    >>>heap = [5, 1, 2, 4, 0, 8, 7, 1, 10]
    >>>build_max_heap(heap)
    >>>max_heap_insert(heap, 6)
    >>>heap
    [10, 6, 8, 4, 5, 2, 7, 1, 1, 0]
    """
    heap.insert(0, item)
    max_heapify(heap, 0)
    #build_max_heap(heap)

def m(heap, item):
    heap += [item]
    index = 0
    while True:
        left_index = left_child(index)
        right_index = right_child(index)

        print(left_index, heap[left_index])

        if left_index > heap_size(heap):
            break

        index += 1



