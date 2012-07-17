import random
import unittest
import src.sort.binary_search as search

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.in_array = range(20)
   
    def test_search_elemeent_two(self):
        key = 2

        find = search.binary_search( self.in_array, key)  
    
        self.assertEqual(key, find)

    def test_search_not_find_key(self):
        key = 100

        find = search.binary_search( self.in_array, key)

        self.assertEqual(None, find )

    def test_search_empty_in( self ):
        key  = 1

        find = search.binary_search([], key)

        self.assertEqual(None, find )


