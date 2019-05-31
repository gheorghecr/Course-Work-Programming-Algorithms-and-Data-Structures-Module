""" Exercise 3) Implement the structure for an unweighted, undirected graph G, where nodes consist of
positive integers. Also, implement a function isPath(v, w), where v and w are vertices in the
graph, to check if there is a path between the two nodes. The path found will be printed to a
text file as a sequence of integer numbers (the node values)."""

""" Exercise 4) Using the graph structure previously implemented, implement a function isConnected(G) to
check whether or not the graph is strongly connected. The output should be simply 'yes' or 'no'."""

"""Exercise 5 )Implement BFS and DFS traversals for the above graph structure. Save the nodes traversed in
sequence to a text file"""

# node or vertice e o ponto do grafico
# edge is the line between two points that connects them
from collections import defaultdict

class Graph:
    def __init__(self):
        """
            Title: Generate a graph using Dictionary in Python
            Author: Geeksforgeeks
            Date: 2018
            Availability:https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
        """
        self.graph = defaultdict(list)

    def addEdges(self,u,v):
        """Adding the edges between the nodes """
        self.graph[u].append(v)

    def isPath(self,s,w):
        """Exercise 3,  s is the source and w the destination,
        this function will check if there is a path between the two nodes (s and w)

        To complete the exercise I based my self on:
        Title: More Graphs
            Author: Hintea, D.
            Date: 2018
            Availability: http://moodle.coventry.ac.uk
            """
        queue = []
        visited =  []
        path = []
        queue.append(s)
        visited.append(s)
        while queue:
            actual = queue.pop(0)
            path.append(actual)
            if actual == w:
                return True,path
            for i in self.graph[actual]:
                if (i not in visited):
                    queue.append(i)
                    visited.append(i)
        return False, path

    def DFS(self,v):
        """Exercise 5, implementation of the Depth First Search algorithm starting
        from a node (v), returning the nodes visited

        To complete the exercise I based my self on:
        Title: Depth First Search (DFS) - 5 minutes algorithm - python [Imagineer]
            Author: Minsuk Heo
            Date: 2016
            Availability: https://www.youtube.com/watch?v=0Zsabo7ires

        Title: More Graphs
            Author: Hintea, D.
            Date: 2018
            Availability: http://moodle.coventry.ac.uk
        """

        stack = []
        visited =  []
        stack.append(v)
        while stack:
            actual = stack.pop()
            if (actual not in visited):
                visited.append(actual)
                for i in self.graph[actual]:
                    stack.append(i)
        return visited

    def BFS(self,v):
        """Exercise 5, implementation of the Breadth First Search algorithm starting
        from a node (v), returning the nodes visited

        To complete the exercise I based my self on:
        Title: More Graphs
            Author: Hintea, D.
            Date: 2018
            Availability: http://moodle.coventry.ac.uk
        """
        #prints the childs of v first  and then goes to the others
        queue = []
        visited =  []
        queue.append(v)
        while queue:
            actual = queue.pop(0)
            if (actual not in visited):
                visited.append(actual)
                for i in self.graph[actual]:
                    queue.append(i)
        return visited

    def isConnected(self):
        """Exercise 4
        Check if the graph is strongly connected, if from a node is possible to reach
        all the others ondes, returning Yes if it is possible and No if is not possible """
        stack = []
        visited =  []
        stack.append(1)
        while stack:
            actual = stack.pop()
            for i in self.graph[actual]:
                if (i not in visited):
                    stack.append(i)
                    visited.append(i)
        # checking if all the nodes were visited
        for key in self.graph:
            if key not in visited:
                return_value = "No"
                return return_value
        return_value = "Yes"
        return return_value


if __name__ == "__main__":

    def write_path_to_file(fileName,path=[]):
        """function to write to files"""
        try:
            f = open ( fileName , "w")
            for node in path:
                f.write(str(node) + "\n")
            f.close()

        except (IOError, OSError):
            print ("Error: File not found.")

    graph = Graph()
    #adding the edges
    graph.addEdges(1,2)
    graph.addEdges(1,3)
    graph.addEdges(2,1)
    graph.addEdges(2,3)
    graph.addEdges(3,1)
    graph.addEdges(3,2)
    graph.addEdges(3,4)
    graph.addEdges(3,5)
    graph.addEdges(4,3)
    graph.addEdges(4,5)
    graph.addEdges(5,3)
    #graph.addEdges(5,6)  #make a connected graph
    graph.addEdges(6,7)
    graph.addEdges(7,6)

    print("The Graph is strongly connected:")
    print(graph.isConnected())

    #check the path between to vertices
    result, path = graph.isPath(1,5)
    print( "There are a path between 1 and 5: " + str(result) + ", the path is "+  str(path))
    #write the path returned from isPath() to a file
    fileName = "isPath.txt"
    write_path_to_file(fileName, path)

    #write the path returned from DFS to a file
    fileNameForDFS = "dfsFile.txt"
    path_dfs = graph.DFS(1)
    write_path_to_file(fileNameForDFS, path_dfs)

    #write the path returned from BFS to a file
    fileNameForBFS = "bfsFile.txt"
    path_bfs = graph.BFS(1)
    write_path_to_file(fileNameForBFS, path_bfs)
