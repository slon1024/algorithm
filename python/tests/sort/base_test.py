import random
import unittest
import sys

sys.setrecursionlimit(100000)

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.in_array = random.sample(range(0, 10000), 1000)
        self.expected_array = sorted(self.in_array)
