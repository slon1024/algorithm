package sort
import "testing"

func TestMergeSortEmptyInput(t *testing.T) {
    values := []int{}
    baseTest(values, t)
}

func TestMergeSortBigData(t *testing.T) {
    baseTest(genBigArray(), t)
}

func TestMergeSortNegativeValues(t *testing.T) {
    values := []int{-3, -5, -1, -15}
    baseTest(values, t)
}