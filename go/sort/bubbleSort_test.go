package sort

import (
    "math/rand"
    "sort"
    "testing"
)

func TestEmptyInput(t *testing.T) {
    values := []int{}

    baseTest(values, t)
}

func TestBigData(t *testing.T) {
    values := make([]int, 1000)
    for i := 0; i < len(values); i++ {
        values[i] = rand.Intn(100000)
    }

    baseTest(values, t)
}

func TestNegativeValues(t *testing.T) {
    values := []int{-3, -5, -1, -15}

    baseTest(values, t)
}

func baseTest(values []int, t *testing.T) {
    actualValues := BubleSort(values)
    areSorted := sort.IntsAreSorted(actualValues)

    if areSorted == false {
        sort.Ints(values)
        t.Errorf("There're not sorted. Actual values: %v, expected values: %v", actualValues, values)
    }
}
