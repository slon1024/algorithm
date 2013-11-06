package sort

func MergeSort(inArray []int) []int {
    if len(inArray) < 2 {
        return inArray
    }

    middle := len(inArray) >> 1
    left := MergeSort(inArray[middle:])
    right := MergeSort(inArray[:middle])

    return merge(left, right)
}

func merge(left []int, right []int) []int {
    result := make([]int, len(left) + len(right))
    var index int;

    for index = 0; len(left) > 0 && len(right) > 0; index++ {
        if (left[0] < right[0]) {
            result[index] = left[0]
            left = left[1:]
        } else {
            result[index] = right[0]
            right = right[1:]
        }
    }

    mergeRest(left, result, index)
    mergeRest(right, result, index)

    return result
}

func mergeRest(rest []int, result []int, index int) {
    for _, val := range rest {
        result[index] = val
        index += 1
    }     
}