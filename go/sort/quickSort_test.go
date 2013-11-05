package sort
import "testing"

func TestEmptyInput(t *testing.T) {
    values := []int{}
    baseTest(values, t)
}

func TestBigData(t *testing.T) {
    baseTest(genBigArray(), t)
}

func TestNegativeValues(t *testing.T) {
    values := []int{-3, -5, -1, -15}
    baseTest(values, t)
}