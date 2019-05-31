import unittest
from ex6 import Graph


class TesteEx6(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        #init method is inialized for each time that a test is run
        super(TesteEx6, self).__init__(*args, **kwargs)      
        self.graph = Graph()
        self.graph.addEdges(1,2,3)
        self.graph.addEdges(1,3,2)
        self.graph.addEdges(2,1,3)
        self.graph.addEdges(2,3,6)
        self.graph.addEdges(3,1,2)
        self.graph.addEdges(3,2,6)
        self.graph.addEdges(3,4,5)
        self.graph.addEdges(3,5,7)
        self.graph.addEdges(4,3,5)
        self.graph.addEdges(4,5,3)
        self.graph.addEdges(5,3,7)
        self.graph.addEdges(5,4,3)

    def test_dijkstra(self):
        """Testing the dijkstra function"""
        path, minDistance = self.graph.dijkstra(1,5)
        self.assertEqual(path,[1,3,5])
        self.assertEqual(minDistance,9)


if __name__ == '__main__':
    unittest.main()
