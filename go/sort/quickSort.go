package sort

func QuickSort(inArray []int) []int {
    if len(inArray) < 2 {
        return inArray
    }

    return quickSortInner(inArray, 0, len(inArray)-1)
}

func quickSortInner(inArray []int, start int, finish int) []int {
    if (start > finish) {
        return inArray
    }

    pivotIndex := getPivot(start, finish)
    pivot := inArray[pivotIndex]

    swap(inArray, pivotIndex, finish)

    lessIndex := start
    for greaterIndex := start; greaterIndex < finish; greaterIndex++ {
        if inArray[greaterIndex] < pivot {
            swap(inArray, lessIndex, greaterIndex)
            lessIndex += 1
        }
    }

    swap(inArray, lessIndex, finish)
    quickSortInner(inArray, start, lessIndex-1)
    quickSortInner(inArray, lessIndex+1, finish)

    return inArray
}

func swap(inArray []int, firstIndex int, secondIndex int) {
    inArray[firstIndex], inArray[secondIndex] = 
    inArray[secondIndex], inArray[firstIndex]
}

func getPivot(start int, finish int) int {
    return ((finish - start) >> 1) + start
}