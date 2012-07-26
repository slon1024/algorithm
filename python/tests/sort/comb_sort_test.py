import random
import unittest
import src.sort.comb_sort as sort
    
class TestCombSort(unittest.TestCase):
    def setUp(self):
        self.in_array = random.sample(range(0, 100), 20)

    def test_sort(self):
        expected_array = sorted(self.in_array)
        result_array   = sort.comb_sort( self.in_array)  
    
        self.assertEqual(expected_array, result_array )

if __name__ == '__main__':
    unittest.main()


