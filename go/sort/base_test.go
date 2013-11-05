package sort

import (
    "sort"
    "testing"
    "math/rand"
)

func genBigArray() [] int{
    values := make([]int, 1000)
    for i := 0; i < len(values); i++ {
        values[i] = rand.Intn(100000)
    }

    return values
}

func baseTest(values []int, t *testing.T) {
    actualValues := BubleSort(values)
    areSorted := sort.IntsAreSorted(actualValues)

    if areSorted == false {
        sort.Ints(values)
        t.Errorf("There're not sorted. Actual values: %v, expected values: %v", actualValues, values)
    }
}