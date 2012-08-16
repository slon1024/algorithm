from tests.sort.base_test import BaseTest
import src.sort.heap_sort as sort



class TestHeapSort(BaseTest):

    def test_sort(self):
        result_array  = sort.heap_sort(self.in_array)

        self.assertEqual(self.expected_array, result_array )

