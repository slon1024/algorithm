from tests.sort.base_test import BaseTest
from src.sort.odd_even_sort import odd_even_sort

class TestBubbleSort(BaseTest):
    def test_sort(self):
        expected_array = sorted(self.in_array)
        result_array   = odd_even_sort( self.in_array)

        self.assertEqual(expected_array, result_array )

if __name__ == '__main__':
    BaseTest.main()