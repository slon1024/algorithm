package sort
import "testing"

func TestQuickSortEmptyInput(t *testing.T) {
    values := []int{}
    baseTest(values, t)
}

func TestQuickSortBigData(t *testing.T) {
    baseTest(genBigArray(), t)
}

func TestQuickSortNegativeValues(t *testing.T) {
    values := []int{-3, -5, -1, -15}
    baseTest(values, t)
}