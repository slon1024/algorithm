from tests.sort.base_test import BaseTest
import src.sort.strand_sort as sort
    
class TestStrandSort(BaseTest):
    def sort(self, in_array):
        return sort.strand_sort(in_array)

    def test_empty_input(self):
        self.assertEqual([], self.sort( [] ))

    def test_big_input_data(self):
        self.assertEqual(self.expected_array, self.sort(self.in_array) )

    def test_positive_float(self):
        expected = [0., 1., 2., 3.]
        self.assertEqual(expected, self.sort( [2., 3., 1., 0.]) )

    def test_negative_float(self):
        expected = [-2., 0., 1., 3.]
        self.assertEqual(expected, self.sort( [-2., 3., 1., 0.]) )

    def test_negative_integer(self):
        expected = [-5, 1, 5]
        self.assertEqual(expected, self.sort( [5, 1, -5]) )

    def test_string(self):
        expected = ['a', 'b', 'f']
        self.assertEqual(expected, self.sort( ['b', 'a', 'f'] ) )

if __name__ == '__main__':
    BaseTest.main()