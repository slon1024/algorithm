from tests.sort.base_test import BaseTest
import src.sort.quick_sort as sort
    
class TestQuickSort(BaseTest):
    def test_sort(self):
        expected_array = sorted(self.in_array)
        result_array   = sort.quick_sort( self.in_array[:])  
    
        self.assertEqual(expected_array, result_array )

if __name__ == '__main__':
    BaseTest.main()


