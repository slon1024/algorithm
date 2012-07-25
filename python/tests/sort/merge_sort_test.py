import random
import unittest
import src.sort.merge_sort as sort

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.in_array = random.sample(range(0, 100), 20)
        self.expected_array = sorted(self.in_array)

    def test_sort(self):
        result_array  = sort.merge_sort( self.in_array)  
    
        self.assertEqual(self.expected_array, result_array )


