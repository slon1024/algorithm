import unittest
import src.graph.kruskal as graph

class TestKruskal(unittest.TestCase):

    def test_graph(self):
        nodes=list("ABCDEFGHI")
        edges=[
            ('A', 'B', 4), ('B', 'C', 12), ('C', 'D', 7),
            ('D', 'E', 9), ('E', 'F', 10), ('F', 'G', 2),
            ('G', 'H', 1), ('H', 'A', 8), ('H', 'B', 11),
            ('H', 'I', 7), ('G', 'I', 6), ('I', 'C', 2),
            ('C', 'F', 4), ('D', 'F', 14)
        ]

        expected=[('G', 'H', 1), ('F', 'G', 2), ('I', 'C', 2), ('A', 'B', 4), ('C', 'F', 4), ('C', 'D', 7), ('H', 'A', 8), ('D', 'E', 9)]
        result_graph  = graph.kruskal(nodes, edges)  
        
        self.assertEqual(expected, result_graph )