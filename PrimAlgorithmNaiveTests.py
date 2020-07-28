import unittest
from AdjaciencyListEdge import Edge
from PrimAlgorithmNaive import PrimAlgorithmNaive

class PrimAlgoNaiveTests(unittest.TestCase):
    def test_normal_graph(self):
        matrix = [[Edge(0, 1, 1), Edge(0, 2, 4), Edge(0, 3, 3)],
                  [Edge(1, 0, 1), Edge(1, 3, 2)],
                  [Edge(2, 0, 4), Edge(2, 3, 5)],
                  [Edge(3, 0, 3), Edge(3, 1, 2), Edge(3, 2, 5)]]
        
        result = PrimAlgorithmNaive().findMinimumSpanningTree(matrix)
        self.assertIn(Edge(0, 1, 1), result[0])
        self.assertIn(Edge(0, 2, 4), result[0])
        self.assertIn(Edge(1, 3, 2), result[1])
        
    def empty_graph(self):
        matrix = [[]]
        result = PrimAlgorithmNaive().findMinimumSpanningTree(matrix)
        self.assertIs(0, len(result))