package sort
import "testing"

func TestSelectionSortEmptyInput(t *testing.T) {
    values := []int{}
    baseTest(values, t)
}

func TestSelectionSortBigData(t *testing.T) {
    baseTest(genBigArray(), t)
}

func TestSelectionSortNegativeValues(t *testing.T) {
    values := []int{-3, -5, -1, -15}
    baseTest(values, t)
}