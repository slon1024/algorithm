from tests.sort.base_test import BaseTest
import src.sort.reverse_inserion_sort as sort

class TestInsertionSort(BaseTest):
    def sort(self, in_array):
        return sort.reverse_inserion_sort(in_array)

    def test_empty_input(self):
        self.assertEqual([], self.sort( [] ))

    def test_big_input_data(self):
        self.expected_array = self.expected_array[::-1]
        result_array = sort.reverse_inserion_sort( self.in_array )

        self.assertEquals( self.expected_array, result_array )

    def test_positive_float(self):
        expected = [3., 2., 1., 0.]
        self.assertEqual(expected, self.sort( [2., 3., 1., 0.]) )

    def test_negative_float(self):
        expected = [3., 1., 0., -2]
        self.assertEqual(expected, self.sort( [-2., 3., 1., 0.]) )

    def test_negative_integer(self):
        expected = [5, 1, -5]
        self.assertEqual(expected, self.sort( [5, 1, -5]) )

    def test_string(self):
        expected = ['f', 'b', 'a']
        self.assertEqual(expected, self.sort( ['b', 'a', 'f'] ) )

if __name__ == '__main__':
    BaseTest.main()