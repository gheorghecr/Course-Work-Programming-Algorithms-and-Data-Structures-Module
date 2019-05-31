import unittest
from ex3 import Graph


class TesteEx3(unittest.TestCase):

    def __init__(self, *args, **kwargs):
         #init method is inialized for each time that a test is run
        super(TesteEx3, self).__init__(*args, **kwargs)
        self.graph = Graph()
        self.graph.addEdges(1,2)
        self.graph.addEdges(1,3)
        self.graph.addEdges(2,1)
        self.graph.addEdges(2,3)
        self.graph.addEdges(3,1)
        self.graph.addEdges(3,2)
        self.graph.addEdges(3,4)
        self.graph.addEdges(3,5)
        self.graph.addEdges(4,3)
        self.graph.addEdges(4,5)
        self.graph.addEdges(5,3)
        #graph.addEdges(5,6)  #make a connected graph
        self.graph.addEdges(6,7)
        self.graph.addEdges(7,6)

    def test_isPath(self):
        """Testing the IsPath function"""
        result, path = self.graph.isPath(1,5)
        self.assertEqual(path,[1,2,3,4,5])
        self.assertEqual(result,True)
        result, path = self.graph.isPath(1,7)
        self.assertEqual(path,[1,2,3,4,5])
        self.assertEqual(result,False)

    def test_DFS(self):
        """Testing the DFS function"""
        visited = self.graph.DFS(2)
        self.assertEqual(visited,[2,3,5,4,1])

    def test_BFS(self):
        """Testing the BFS function"""
        visited = self.graph.BFS(4)
        self.assertEqual(visited,[4,3,5,1,2])

    def test_isConnected(self):
        """Testing the isConnected function"""
        result = self.graph.isConnected()
        self.assertEqual(result,"No")


if __name__ == '__main__':
    unittest.main()
