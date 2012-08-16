from tests.sort.base_test import BaseTest
import src.sort.recursion_insertion_sort as sort

class TestInsertionSort(BaseTest):
    def test_sort(self):
        result_array  = sort.recursion_insertion_sort( self.in_array)  
    
        self.assertEqual(self.expected_array, result_array )

if __name__ == '__main__':
    BaseTest.main()