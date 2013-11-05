package sort

func BubleSort(inArray []int) []int {
    length := len(inArray)
    for i := 0; i < length-1; i++ {
        for j := i + 1; j < length; j++ {
            if inArray[j] < inArray[i] {
                inArray[i], inArray[j] = inArray[j], inArray[i]
            }
        }
    }

    return inArray
}
