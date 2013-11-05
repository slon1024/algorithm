package sort
import "testing"

func TestBubleSortEmptyInput(t *testing.T) {
    values := []int{}
    baseTest(values, t)
}

func TestBubleSortBigData(t *testing.T) {
    baseTest(genBigArray(), t)
}

func TestBubleSortNegativeValues(t *testing.T) {
    values := []int{-3, -5, -1, -15}
    baseTest(values, t)
}
