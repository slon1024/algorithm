from tests.sort.base_test import BaseTest
import src.sort.reverse_inserion_sort as sort

class TestInsertionSort(BaseTest):

    def test_reverse_sort(self):
        self.expected_array = self.expected_array[::-1]
        result_array = sort.reverse_inserion_sort( self.in_array )
    
        self.assertEquals( self.expected_array, result_array )

if __name__ == '__main__':
    BaseTest.main()