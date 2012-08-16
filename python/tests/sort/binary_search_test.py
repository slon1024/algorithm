from tests.sort.base_test import BaseTest
import src.sort.binary_search as search

class TestInsertionSort(BaseTest):

    def test_search_empty_in( self ):
        key  = 1

        find = search.binary_search([], key)

        self.assertEqual(None, find )


if __name__ == '__main__':
    BaseTest.main()

