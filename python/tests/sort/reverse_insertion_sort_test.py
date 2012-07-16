import random
import unittest
import src.sort.reverse_inserion_sort as sort

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.in_array = random.sample(range(0, 100), 20)
        self.expected_array = sorted(self.in_array)
        self.expected_array = self.expected_array[::-1]


    def test_reverse_sort(self):
        result_array = sort.reverse_inserion_sort( self.in_array )
    
        self.assertEquals( self.expected_array, result_array ) 



