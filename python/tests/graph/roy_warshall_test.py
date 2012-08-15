import random
import unittest
import src.graph.roy_warshall as graph

class TestRoyWarshall(unittest.TestCase):

    def test_graph(self):
        in_graph=[ 
            [0,1,0,1,0], 
            [0,0,0,1,0], 
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,1,0,0,0]
        ]

        expected=[
            [0,1,1,1,0],
            [0,1,1,1,0],
            [0,1,1,1,0],
            [0,1,1,1,0],
            [0,1,1,1,0]
        ]

        result_graph  = graph.roy_warshall(in_graph)  
    
        self.assertEqual(expected, result_graph )
