import random
import unittest
import sys

sys.setrecursionlimit(100000)

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.in_array = random.sample(range(0, 100000), 100)
        self.expected_array = sorted(self.in_array)

