from tests.sort.base_test import BaseTest
from src.sort.counting_sort import counting_sort


class TestStrandSort(BaseTest):

    def test_sort(self):
        expected_array = sorted(self.in_array)
        result_array   = counting_sort( self.in_array)

        self.assertEqual(expected_array, result_array )

if __name__ == '__main__':
    BaseTest.main()