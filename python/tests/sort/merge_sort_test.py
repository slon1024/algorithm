from tests.sort.base_test import BaseTest
import src.sort.merge_sort as sort

class TestMergeSort(BaseTest):

    def test_sort(self):
        result_array  = sort.merge_sort( self.in_array)  
    
        self.assertEqual(self.expected_array, result_array )

if __name__ == '__main__':
    BaseTest.main()