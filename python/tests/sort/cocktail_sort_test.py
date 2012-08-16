from tests.sort.base_test import BaseTest
import src.sort.cocktail_sort as sort
   
class TestCocktailSort(BaseTest):
    def test_sort(self):
        expected_array = sorted(self.in_array)
        result_array   = sort.cocktail_sort( self.in_array)  
    
        self.assertEqual(expected_array, result_array )

if __name__ == '__main__':
    BaseTest.main()


