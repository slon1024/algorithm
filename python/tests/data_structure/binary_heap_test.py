import unittest
import data_structure.binary_heap as binary_heap
import random

class TestBinaryHeap(unittest.TestCase):

    def test_heap_size_should_be_zero(self):
        A = []

        actual=binary_heap.heap_size(A)
        expected = 0

        self.assertEqual(actual, expected)

    def test_parent_index(self):
        actual = binary_heap.parent(9)
        expected = 4

        self.assertEqual(actual, expected)

    def test_left_index(self):
        actual = binary_heap.left_child(3)
        expected = 7

        self.assertEqual(actual, expected)

    def test_right_index(self):

        actual = binary_heap.right_child(4)
        expected = 10

        self.assertEqual(actual, expected)

    def test_max_heapify(self):
        heap = [5, 1, 2, 4, 0, 8, 7, 1, 10]

        binary_heap.max_heapify(heap, 1)
        expected = [5, 4, 2, 10, 0, 8, 7, 1, 1]


        self.assertEqual(heap, expected)

    def test_build_heap_max(self):
        heap = [5, 1, 2, 4, 0, 8, 7, 1, 10]

        binary_heap.build_max_heap(heap)
        expected = [10, 5, 8, 4, 0, 2, 7, 1, 1]

        self.assertEqual(heap, expected)

    def test_heap_sort(self):
        heap = [random.randint(1, 100000) for x in range(100)]
        expected = sorted(heap[:], reverse=True)

        actual = binary_heap.max_heap_sort(heap)

        self.assertEqual(actual, expected)


    def test_max_heap_insert(self):
        max_value = 50
        heap = [random.randint(1, max_value) for x in range(10)]
        new_item = random.randint(1, max_value)
        expected = heap + [new_item]
        binary_heap.build_max_heap( expected )
    #    print(heap, new_item)
        binary_heap.build_max_heap(heap)
        binary_heap.max_heap_insert(heap, new_item)

        self.assertEqual(heap, expected)

        #heap = [5, 1, 2, 4, 0, 8, 7, 1, 10]
        #binary_heap.build_max_heap(heap)
        #binary_heap.m(heap, 6)
        #print(heap)
        #binary_heap.build_max_heap(heap)
        #print( heap )

