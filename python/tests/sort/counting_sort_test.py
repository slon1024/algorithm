from tests.sort.base_test import BaseTest
import src.sort.counting_sort as sort

class TestCountingSort(BaseTest):
    def sort(self, in_array):
        return sort.counting_sort(in_array)

    def test_empty_input(self):
        self.assertEqual([], self.sort( [] ))

    def test_big_input_data(self):
        self.assertEqual(self.expected_array, self.sort(self.in_array) )

    def test_positive_float(self):
        self.assertRaises(TypeError, sort.counting_sort, [2., 3., 1., 0.])

    def test_negative_float(self):
        self.assertRaises(TypeError, sort.counting_sort, [2., 3., 1., 0.])

    def test_negative_integer(self):
        expected = [-5, 1, 5]
        self.assertEqual(expected, self.sort( [5, 1, -5]) )

    def test_string_should_be_raise(self):
        self.assertRaises(TypeError, sort.counting_sort, ['b', 'a'])

if __name__ == '__main__':
    BaseTest.main()