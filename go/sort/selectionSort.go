package sort

func SelectionSort(inArray []int) []int {
    length := len(inArray)
    for outerIndex := 0; outerIndex < length - 1; outerIndex++ {
        minIndex := outerIndex
        for innerIndex := outerIndex + 1; innerIndex < length; innerIndex++ {
           if inArray[minIndex] > inArray[innerIndex] {
                 minIndex = innerIndex
            }
        }

        inArray[outerIndex], inArray[minIndex] = 
                inArray[minIndex], inArray[outerIndex]
    }
   return inArray
}