from tests.sort.base_test import BaseTest
import src.sort.radix_sort as sort

class TestRadixSort(BaseTest):
    def sort(self, in_array):
        return sort.radix_sort(in_array)

    def test_empty_input(self):
        self.assertEqual([], self.sort( [] ))

    def test_big_input_data(self):
        self.assertEqual(self.expected_array, self.sort(self.in_array) )

    def test_positive_float(self):
        self.assertRaises(TypeError, sort.radix_sort, [1., 2.])

    def test_negative_float(self):
        self.assertRaises(ValueError, sort.radix_sort, [-1., -3.])

    def test_negative_integer(self):
        self.assertRaises(ValueError, sort.radix_sort, [-1, 2, -3])

    def test_string(self):
        self.assertRaises(TypeError, sort.radix_sort, ['a', 'b'])

if __name__ == '__main__':
    BaseTest.main()